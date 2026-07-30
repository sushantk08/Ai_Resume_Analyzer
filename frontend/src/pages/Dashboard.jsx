import {
    Typography,
    Grid,
    CircularProgress,
    Alert,
    Card,
    CardContent,
} from "@mui/material";

import { useEffect, useState } from "react";

import api from "../api/api";

import MainLayout from "../layouts/MainLayout";

import DashboardCard from "../components/DashboardCard";

export default function Dashboard() {

    const [dashboard, setDashboard] = useState(null);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    useEffect(() => {

        async function fetchDashboard() {

            try {

                const response = await api.get("/dashboard");

                console.log(response.data);

                setDashboard(response.data);

            } catch (err) {

                console.error(err);

                setError("Failed to load dashboard.");

            } finally {

                setLoading(false);

            }

        }

        fetchDashboard();

    }, []);

    return (

        <MainLayout>

            <Typography
                variant="h4"
                gutterBottom
            >
                Dashboard
            </Typography>

            {loading && <CircularProgress />}

            {error && (
                <Alert severity="error">
                    {error}
                </Alert>
            )}

            {dashboard && (

                <>

                    <Grid
                        container
                        spacing={3}
                    >

                        <Grid item xs={12} md={3}>
                            <DashboardCard
                                title="Total Resumes"
                                value={dashboard.total_resumes}
                            />
                        </Grid>

                        <Grid item xs={12} md={3}>
                            <DashboardCard
                                title="Total Jobs"
                                value={dashboard.total_jobs}
                            />
                        </Grid>

                        <Grid item xs={12} md={3}>
                            <DashboardCard
                                title="Total Analyses"
                                value={dashboard.total_analyses}
                            />
                        </Grid>

                        <Grid item xs={12} md={3}>
                            <DashboardCard
                                title="Average ATS"
                                value={`${dashboard.average_score}%`}
                            />
                        </Grid>

                    </Grid>

                    <Card sx={{ mt: 4 }}>

                        <CardContent>

                            <Typography variant="h6">
                                Latest Resume
                            </Typography>

                            {dashboard.latest_resume ? (
                                <>
                                    <Typography>
                                        Name: {dashboard.latest_resume.name}
                                    </Typography>

                                    <Typography>
                                        Email: {dashboard.latest_resume.email}
                                    </Typography>
                                </>
                            ) : (
                                <Typography>
                                    No resumes uploaded yet.
                                </Typography>
                            )}

                        </CardContent>

                    </Card>

                </>

            )}

        </MainLayout>

    );

}