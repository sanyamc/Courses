import * as React from 'react';
import { Component } from 'react'; // pull off single property instead of entire object
import {Button, ButtonGroup, DropdownButton, Input, Navbar, Nav, NavItem, NavDropdown, MenuItem, ProgressBar, Glyphicon, Grid, Row, Col, FormControl, InputGroup, Panel} from 'react-bootstrap';
import {browserHistory, Redirect, Link} from 'react-router';
import { bindActionCreators } from 'redux';
import {connect} from 'react-redux'
import { getEngagementData } from '../actions/getData';
import { toggleSidebar } from '../actions/layout';


import SideBarLinkItem from '../components/sidebarLink';
import Summary from '../components/Summary';

class App extends Component<any,any>{
constructor(props) {
        super(props);
        this.toggleSidebar = this.toggleSidebar.bind(this);
        //console.log(this.props);
        this.props.getEngagementData();
    }
    
    toggleSidebar(e:any) {
        e.preventDefault();        
        this.props.toggleSidebar();
    }
    
  /*  getEngagementData(e){
        e.preventDefault();
        this.summaryData=this.props.getEngagementData();
        console.log(this.props.getEngagementData);
    }*/
	render(){        
         let props = this.props;
       // var filters = this.props.filters;       
        let sidebarOpen = this.props.layout.sidebarOpen;
        let sidebarClass = sidebarOpen ? "sidebar" : "sidebar compact";
        let viewContainerClass = sidebarOpen ? "view-container" : "view-container sidebar-compact";
        let sidebarSliderbtnClass = sidebarOpen ? "glyphicon glyphicon-triangle-left" : "glyphicon glyphicon-triangle-right";
        let isDisplayModeMinimal=false;
        
        let row1HeightStyle = { height: '650px' };
        let row2HeightStyle = { height: '380px' };
        let row3HeightStyle = { height: '380px' };
        let row4HeightStyle = { height: '320px' };
        let row5HeightStyle = { height: '320px' };
        
       // console.log(this.props.summary);
       let summaryView:any;
       /*console.log('data '+JSON.stringify(this.props.summary.data));
       if(this.props.summary.data!=null){
          summaryView= <Summary data ={this.props.summary.data} />;
       }
       else{
           summaryView=<div></div>;
       }*/
       
		return(
        <div>
        <Navbar className="site-header">
                    <Navbar.Header>
                        <Navbar.Brand>
                           <span className="logo-title">ADvENT</span>
                        </Navbar.Brand>
                    </Navbar.Header>
                    <Nav style={{ margin: 0 }} pullRight>
                        <NavItem href="http://whodogfoods" target="_blank">WD</NavItem>
                        <NavItem href="http://heatmaps" target="_blank">HM</NavItem>
                      {/*    <NavItem href="#"><span className="glyphicon glyphicon-comment" /></NavItem>
                        <li>
                            <Dropdown id="dataDisplayModeDropdown">
                                <Dropdown.Toggle noCaret>
                                    <span className="glyphicon glyphicon-cog" />
                                </Dropdown.Toggle>
                              <Dropdown.Menu>
                                    <MenuItem header>Data display mode</MenuItem>
                                    <MenuItem className={"pad-left-20" + (isDisplayModeMinimal ? " checked" : " unchecked") } eventKey={"data-display-mode-minimal"} onSelect={this.handleSettingChange.bind(this) }>Minimal</MenuItem>
                                    <MenuItem className={"pad-left-20" + (isDisplayModeMinimal ? " unchecked" : " checked") } eventKey={"data-display-mode-full"} onSelect={this.handleSettingChange.bind(this) }>Full</MenuItem>
                                </Dropdown.Menu>
                            </Dropdown>
                        </li>
                        <li>
                            <img ref="userImage" className="current-user-image" src={this.props.layout.userImageUrl} onError={this.inavlidUrlFound.bind(this) } />
                        </li>*/}
                    </Nav>
                </Navbar>
        
		 <div className={sidebarClass}>
                    <div className="slide-left-btn-container-side" onClick={this.toggleSidebar}>
                        <span className={sidebarSliderbtnClass}></span>
                        <span className={sidebarSliderbtnClass}></span>
                    </div>
                  <ul>
                        <SideBarLinkItem title="Summary" icon="fa fa-tachometer" isExpanded={sidebarOpen} url="http://bing.com" isActive="true" ></SideBarLinkItem>
                        <SideBarLinkItem title="Adoption" icon="fa fa-download" isExpanded={sidebarOpen} url="http://bing.com" isActive="false" ></SideBarLinkItem>
                        <SideBarLinkItem title="Engagement" icon="fa fa-comments-o" isExpanded={sidebarOpen} url="http://bing.com" isActive="false" ></SideBarLinkItem>                        
                        <div className="sidebar-separator"></div>
                       
                  </ul> 
          </div>
                                {/* Views (tab contents) */}
                 <div className={viewContainerClass}>
                    
                        {/* View header */}
                        <div ref="viewHeader" className="view-header row form-inline">
                            <Navbar>
                                <Navbar.Header>Summary</Navbar.Header>
                               
                            </Navbar>
                            
                        </div>
             {/* View content */}
             
             <div ref="viewContent" className="view-content">                        
                        
                        <div className="container"> 
                          <div className="row top-row">
                            <div className="col-md-12 col-sm-12" style={row1HeightStyle}>
                              {/* User adoption */}
                                <div className="full-height">
                                  <Panel className="base-panel" header="Engagement Charts for Visual Studio">
                                     <div className="col-md-6 full-height hasTitle" >
                                    {/* Engagement chart */}
                                    <div className="chart-title">VS 12 Engagement data</div>
                                    <Summary data ={this.props.summary.data} />                                    
                                    </div>
                                  </Panel>
                                  </div>
                                 </div>
                             </div>
                          </div>        
                        </div>
              </div>
                    
         </div>
               
           
		);
	}
}


function mapDispatchToProps(dispatch){
    return bindActionCreators({ toggleSidebar,getEngagementData },dispatch);
}

function mapStateToProps(state){      
    return { // this will be props in above class 
        layout:state.layout,
        summary:state.summary
    };    
}

export default connect(mapStateToProps,mapDispatchToProps)(App);