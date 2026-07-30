import { Typography, Button } from "@mui/material";
import { Link } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

export default function NotFound() {
    return (
        <MainLayout>
            <Typography variant="h2">
                404
            </Typography>

            <Typography variant="h5">
                Page Not Found
            </Typography>

            <Button
                component={Link}
                to="/"
                variant="contained"
                sx={{ mt: 3 }}
            >
                Go Home
            </Button>
        </MainLayout>
    );
}