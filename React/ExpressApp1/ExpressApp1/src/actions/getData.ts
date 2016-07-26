// file to get data via ajax from micro-services

import * as actionTypes from "../constants/actionTypes";


export function getEngagementData(){
    //console.log('payload '+JSON.stringify(payload));
	return {
		type:actionTypes.GET_ENGAGEMENTDATA,
        payload:payload
	};
    
    
}



let payload = [
{
    "result":
    {
        "data": [
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 590956
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 255487
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 821058
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 833095
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 144189
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 645366
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 740207
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 624806
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 187509
        }
        ,
        {
            "StateWindowStartDate": "2015-12-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 131860
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 935073
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 170232
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 302219
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 660647
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 826602
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 191332
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 133712
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 653930
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 663498
        }
        ,
        {
            "StateWindowStartDate": "2015-11-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 677158
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 774900
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 660920
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 161466
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 926252
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 294664
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 591092
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 589892
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 102512
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 492192
        }
        ,
        {
            "StateWindowStartDate": "2015-10-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 150414
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 751139
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 875179
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 225924
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 788188
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 278767
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 15,
            "sum_NormalizedUsers": 10
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 15,
            "sum_NormalizedUsers": 556
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 814759
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 585286
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 247238
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 148996
        }
        ,
        {
            "StateWindowStartDate": "2016-03-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 651185
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 245994
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 634621
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 774945
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 149601
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 823602
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 796193
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 782207
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 788433
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 248676
        }
        ,
        {
            "StateWindowStartDate": "2016-02-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 200083
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 213239
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 609421
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 804682
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 825195
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 12,
            "sum_NormalizedUsers": 118726
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "Churned",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 757187
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "Exploring",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 698487
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "Active",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 700378
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "DeeplyEngaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 137173
        }
        ,
        {
            "StateWindowStartDate": "2016-01-01T00:00:00Z",
            "CurrentState": "Engaged",
            "VsMajorVersion": 14,
            "sum_NormalizedUsers": 192462
        }
        ]
    }
  }
];