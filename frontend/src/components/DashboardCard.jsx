import { Card, CardContent, Typography } from "@mui/material";

export default function DashboardCard({
    title,
    value,
}) {
    return (
        <Card
            elevation={3}
            sx={{
                borderRadius: 3,
                height: "100%",
            }}
        >
            <CardContent>

                <Typography
                    color="text.secondary"
                    gutterBottom
                >
                    {title}
                </Typography>

                <Typography
                    variant="h4"
                    fontWeight="bold"
                >
                    {value}
                </Typography>

            </CardContent>
        </Card>
    );
}