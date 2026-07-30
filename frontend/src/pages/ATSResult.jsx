import { useLocation } from "react-router-dom";

import {
    Card,
    CardContent,
    Chip,
    Grid,
    Typography,
} from "@mui/material";

import MainLayout from "../layouts/MainLayout";

export default function ATSResult() {

    const { state } = useLocation();

    if (!state) {

        return (
            <MainLayout>
                <Typography>
                    No ATS result found.
                </Typography>
            </MainLayout>
        );

    }

    return (

        <MainLayout>

            <Typography
                variant="h4"
                gutterBottom
            >
                ATS Analysis
            </Typography>

            <Grid
                container
                spacing={3}
            >

                <Grid
                    item
                    xs={12}
                    md={6}
                >

                    <Card>

                        <CardContent>

                            <Typography variant="h5">
                                ATS Score
                            </Typography>

                            <Typography
                                variant="h2"
                                color="primary"
                            >
                                {state.ats_score}%
                            </Typography>

                        </CardContent>

                    </Card>

                </Grid>

                <Grid
                    item
                    xs={12}
                    md={6}
                >

                    <Card>

                        <CardContent>

                            <Typography variant="h6">
                                Candidate
                            </Typography>

                            <Typography>
                                {state.candidate_name}
                            </Typography>

                            <Typography sx={{ mt: 2 }}>
                                {state.company}
                            </Typography>

                        </CardContent>

                    </Card>

                </Grid>

            </Grid>

            <Typography
                variant="h5"
                sx={{ mt: 4 }}
            >
                Matched Skills
            </Typography>

            {state.matched_skills.map((skill) => (

                <Chip
                    key={skill}
                    label={skill}
                    color="success"
                    sx={{ mr: 1, mt: 1 }}
                />

            ))}

            <Typography
                variant="h5"
                sx={{ mt: 4 }}
            >
                Missing Skills
            </Typography>

            {state.missing_skills.map((skill) => (

                <Chip
                    key={skill}
                    label={skill}
                    color="error"
                    sx={{ mr: 1, mt: 1 }}
                />

            ))}

        </MainLayout>

    );

}