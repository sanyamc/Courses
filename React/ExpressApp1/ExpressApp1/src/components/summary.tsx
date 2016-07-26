import * as React from 'react';
import { Component } from 'react';
import * as NVD3Chart from 'react-nvd3';

//import SideBarLinkItem from '../components/sidebarLink';

/*
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
*/


 export default class Summary extends Component<any,any>{	
     
     
     getChartData(){
        // console.log('called '+JSON.stringify(this.props.data[0].result));
         let data= this.props.data[0].result.data;
         let result=[{key:"Engagement Data",values:[]}];
         data.map(function(val){
        if(val.VsMajorVersion==12){
           
            result[0].values.push(val);
        }
    });
   // console.log('called '+ JSON.stringify(result));
    return result;    
}  

render(){
    console.log(this.props);
       // console.log(JSON.stringify(this.data));
        if(!this.props.data){
            return(
            <div>
                 Loading.....
            </div>
        );
        }
        else{   
            // get interesting piece of data    
        this.getChartData=this.getChartData.bind(this);
        return(
            
                <NVD3Chart type="discreteBarChart" id="barChart" datum={this.getChartData}
                 x="StateWindowStartDate"
                 y="sum_NormalizedUsers"
                 
                />
            
        );
        
        }
        
    
    }
 }

