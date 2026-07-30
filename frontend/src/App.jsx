import { Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import UploadResume from "./pages/UploadResume";
import JobDescription from "./pages/JobDescription";
import ATSResult from "./pages/ATSResult";
import AIAnalysis from "./pages/AIAnalysis";
import InterviewQuestions from "./pages/InterviewQuestions";
import ResumeRewrite from "./pages/ResumeRewrite";
import KeywordSuggestions from "./pages/KeywordSuggestions";
import NotFound from "./pages/NotFound";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />

      <Route path="/upload" element={<UploadResume />} />

      <Route path="/job" element={<JobDescription />} />

      <Route path="/result" element={<ATSResult />} />

      <Route path="/analysis" element={<AIAnalysis />} />

      <Route path="/interview" element={<InterviewQuestions />} />

      <Route path="/rewrite" element={<ResumeRewrite />} />

      <Route path="/keywords" element={<KeywordSuggestions />} />

      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}