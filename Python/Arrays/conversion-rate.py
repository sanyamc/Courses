export function testD3(origData, transfer, newKeys = ["% of Stage 1", "% of Stage 2"]) {
    let conversionStats = [];
    try {
        
        let transfer = ["Stage 1 - Attempted Install", "Stage 2 - Successful Install","Stage 3 - Launched VS"];
        let grouped = d3.nest() // returns a new array
        .key(function(d:any){return d.AdoptionDate; })  // group by date for all the stages
        .sortKeys(d3.ascending)
       // .rollup(function(v:any){ return { x: new Date(v.AdoptionDate), y:}}
        .map(origData, d3.map);

        if(grouped.values().length>0){
            // grouped.values().forEach(function(key,value){
            //     // value=[{stage1: x, value:count},{stage2:something,value:count}]
            //     let stage = 
                
            // })
            debugger;
        console.log(JSON.stringify(grouped.values()));
        }


    }
    catch (e) {
        console.error("Error conversion: " + e);
    }
    finally {
        return conversionStats;
    }
}