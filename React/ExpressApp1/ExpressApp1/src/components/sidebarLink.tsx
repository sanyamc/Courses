import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Link } from 'react-router';
import {Tooltip, OverlayTrigger} from "react-bootstrap";

const SideBarLinkItem = ({title, icon, url, isExpanded, isActive}) =>{
           
    const tooltip = <Tooltip id="sideBarTooltip">{title}</Tooltip>;
    let activeClass = isActive ? "active" : "";

    let iconJsx:any;
    if (isExpanded) {
        iconJsx = <span className={icon} />
    } else {
        iconJsx = <OverlayTrigger placement="right" overlay={tooltip}>
            <span className={icon} />
        </OverlayTrigger>
    }
    return (
        <li className={activeClass}>
            <Link to={url}>
                {iconJsx}
                <span className="sidebar-menu-label">{title}</span>
            </Link>
        </li>
    );
    
};

export default SideBarLinkItem;



