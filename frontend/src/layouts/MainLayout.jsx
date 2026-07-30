import { Box } from "@mui/material";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

export default function MainLayout({
    children,
}) {
    return (
        <Box sx={{ display: "flex" }}>

            <Sidebar />

            <Box
                sx={{
                    flexGrow: 1,
                    ml: "240px",
                }}
            >
                <Navbar />

                <Box p={3}>
                    {children}
                </Box>

            </Box>

        </Box>
    );
}