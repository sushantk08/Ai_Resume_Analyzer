import MainLayout from "../layouts/MainLayout";
import { Typography } from "@mui/material";

export default function KeywordSuggestions() {
  return (
    <MainLayout>
      <Typography variant="h4">
        AI Keyword Suggestions
      </Typography>

      <Typography sx={{ mt: 2 }}>
        This page will display AI-generated keyword suggestions.
      </Typography>
    </MainLayout>
  );
}