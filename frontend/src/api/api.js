import axios from "axios";

const api = axios.create({
    baseURL: "https://ai-resume-analyzer-uqtx.onrender.com",
    headers: {
        "Content-Type": "application/json",
    },
});

export default api;