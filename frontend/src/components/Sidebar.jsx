import {
    Drawer,
    List,
    ListItemButton,
    ListItemText,
} from "@mui/material";

import { Link } from "react-router-dom";

const menu = [
    { name: "Dashboard", path: "/" },
    { name: "Upload Resume", path: "/upload" },
    { name: "Job Description", path: "/job" },
    { name: "ATS Result", path: "/result" },
    { name: "AI Analysis", path: "/analysis" },
    { name: "Interview Questions", path: "/interview" },
    { name: "Resume Rewrite", path: "/rewrite" },
];

export default function Sidebar() {
    return (
        <Drawer
            variant="permanent"
            sx={{
                width: 240,
                "& .MuiDrawer-paper": {
                    width: 240,
                },
            }}
        >
            <List>
                {menu.map((item) => (
                    <ListItemButton
                        key={item.name}
                        component={Link}
                        to={item.path}
                    >
                        <ListItemText primary={item.name} />
                    </ListItemButton>
                ))}
            </List>
        </Drawer>
    );
}