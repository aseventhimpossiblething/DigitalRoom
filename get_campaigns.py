
#print("active experiment block------------------------------------------------------------")
from google.protobuf import json_format
import argparse
import sys
import json
import pandas

from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
google_ads_client = GoogleAdsClient.load_from_storage('google-ads.yaml')
ga_service = google_ads_client.get_service('GoogleAdsService', version='v3')

testCampaign="150-063-1476";  
cityAccount="210-489-7739";
cityMobileAccount="423-859-4348";
communityAccount="262-853-2074";
suburbAccount="861-225-9590";
stateAccount="644-879-0580";
hispanicAccount="473-277-5338";
googleArrayOfAccounts=[cityAccount,cityMobileAccount,communityAccount,suburbAccount,stateAccount,hispanicAccount]
googleAccountNumberNameLookup={"210-489-7739":"city","423-859-4348":"cityMobile","262-853-2074":"community","861-225-9590":"suburb",\
                         "644-879-0580":"state","473-277-5338":"hispanic"}

"""
query = ('SELECT campaign.id, campaign.name, campaign.status, campaign_budget.amount_micros,\
metrics.cost_micros, metrics.clicks,  metrics.conversions, metrics.impressions FROM campaign \
WHERE campaign.status="ENABLED" AND segments.date DURING THIS_MONTH ORDER BY campaign.id')
"""

#query = ('SELECT campaign.id, campaign.name FROM campaign WHERE segments.date DURING THIS_MONTH')

#966-289-6891



def fromGoogleAds(customer_id,dateRange):
    
    query = ('SELECT campaign.name,campaign_budget.amount_micros,metrics.cost_micros,\
            metrics.clicks,metrics.conversions,metrics.impressions FROM campaign WHERE \
            campaign.status="ENABLED" AND segments.date DURING '+dateRange)
    """
    query = ('SELECT campaign.id, campaign.name, campaign.status, campaign_budget.amount_micros,\
             metrics.cost_micros, metrics.clicks,  metrics.conversions, metrics.impressions FROM campaign \
            WHERE campaign.status="ENABLED" AND segments.date DURING THIS_MONTH ORDER BY campaign.id')
    """        
    """
    yesterdayQuery = ('SELECT campaign.name, metrics.cost_micros FROM campaign \
           WHERE campaign.status="ENABLED" AND segments.date DURING YESTERDAY')
    """       
          
    
    campaignName=[];
    campaignCost=[];
    campaignClicks=[];
    campaignConversions=[];
    campaignImpressions=[];
    campaignBudget=[];
    campaignStatus=[];
    #yesterdaySpend=[];
    
    newTable={"name":campaignName,"cost":campaignCost,"clicks":campaignClicks,"conversions":\
              campaignConversions,"impressions":campaignImpressions,"budget":campaignBudget,"status":campaignStatus}
    
    #AccntName=accountNumberNameLookup[str(customer_id)];
    #print(AccntName,"=",customer_id); 
    
    customer_id=customer_id.replace("-","") 
    response = ga_service.search_stream(customer_id, query=query) 
    for subset in response:
        jsonObj=json_format.MessageToJson(subset)
        jsonObj=json.loads(jsonObj);
      
        
        countOfSubset=0; 
        numberOfResults=str(subset).count("results");
      
        while numberOfResults>countOfSubset:
         
            try:
               name=jsonObj["results"][countOfSubset]["campaign"]["name"];
               status=jsonObj["results"][countOfSubset]["campaign"]["status"];
               cost=float(jsonObj["results"][countOfSubset]["metrics"]["costMicros"])/1000000;
               clicks=float(jsonObj["results"][countOfSubset]["metrics"]["clicks"]);
               conversions=float(jsonObj["results"][countOfSubset]["metrics"]["conversions"]);
               impressions=float(jsonObj["results"][countOfSubset]["metrics"]["impressions"]);
               budget=float(jsonObj["results"][countOfSubset]["campaignBudget"]["amountMicros"])/100000; 
               #print(type(cost)) 
                
               campaignName.append(name);
               campaignCost.append(cost);
               campaignClicks.append(clicks);
               campaignConversions.append(conversions);
               campaignImpressions.append(impressions);
               campaignBudget.append(budget);
               campaignStatus.append(status);
                                       
               countOfSubset+=1;
           
            except:
               #print("row ",countOfSubset," failed") 
               countOfSubset+=1;
    newTable=pandas.DataFrame(newTable);
    return newTable;       
              
"""  
def googleYesterdayMetrics():
     yesterdayQuery = ('SELECT campaign.name, metrics.cost_micros FROM campaign \
           WHERE campaign.status="ENABLED" AND segments.date DURING YESTERDAY')
"""           
    
  
  
  


#fromAds("150-063-1476",query);
def allAccntCombinedBasedMetrics(googleArrayOfAccounts):
    partialCost=[];
    partialClicks=[];
    partialConversions=[];
    partialImpressions=[];
    partialBudget=[];
    yesterdayCost=[];
    
       
      
    print("in allAccntCombinedBasedMetrics(ArrayOfAccounts)") 
    len(googleArrayOfAccounts);
    count=0;
    for accnts in googleArrayOfAccounts:
       #fromAds(accnts,query); 
       CampaignLevelTable=fromGoogleAds(accnts,"THIS_MONTH"); 
       print(CampaignLevelTable)
       #CampaignLevelTable2=fromGoogleAds(accnts,"YESTERDAY");
       try:
        mtdGoogle=fromGoogleAds(accnts,"THIS_MONTH");
        #yesterdayGoogleCost=fromGoogleAds(accnts,"YESTERDAY");
        cost=sum(mtdGoogle.cost);
        clicks=sum(mtdGoogle.clicks);
        conversions=sum(mtdGoogle.conversions);
        impressions=sum(mtdGoogle.impressions);
        budget=sum(mtdGoogle.budget);
        
        partialCost.append(cost);
        partialClicks.append(clicks);
        partialConversions.append(conversions);
        partialImpressions.append(impressions);
        partialBudget.append(budget);
        yesterdayCost.append(yesterdayGoogleCost);
        
       except:
        print("failed to pull accnt ",accnts," count = ",count)
       count+=1; 
    
    
    partialCost=sum(partialCost);
    partialClicks=sum(partialClicks);
    partialConversions=sum(partialConversions);
    partialImpressions=sum(partialImpressions);
    partialBudget=sum(partialBudget);
    yesterdayCost=sum(yesterdayCost);
    budgetMinusCost=partialBudget-partialCost
    
    
    metrics={"":["Google Ads MTD"],"cost":partialCost,"clicks":partialClicks,"conversions":partialConversions\
       ,"impressions":partialImpressions,"yesterday spend":yesterdayCost,"budget":partialBudget,"remaining budget":budgetMinusCost}
    
    
    metrics=pandas.DataFrame(data=metrics, index=[0])
   
    print(metrics);
    return metrics;
    
#fromAds("150-063-1476",query);     
#googlemetrics=allAccntCombinedBasedMetrics(googleArrayOfAccounts);
#print(googlemetrics.cost)
CampaignLevelTable=fromGoogleAds("210-489-7739","THIS_MONTH"); 
print(CampaignLevelTable)

         
      
      

      
      
     
