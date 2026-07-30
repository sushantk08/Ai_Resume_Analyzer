import { useCallback, useState } from "react";

import { useDropzone } from "react-dropzone";

import {
    Box,
    Button,
    CircularProgress,
    Paper,
    Typography,
} from "@mui/material";

import { toast } from "react-toastify";

import MainLayout from "../layouts/MainLayout";

import api from "../api/api";

export default function UploadResume() {

    const [file, setFile] = useState(null);

    const [loading, setLoading] = useState(false);

    const onDrop = useCallback((acceptedFiles) => {

        if (acceptedFiles.length > 0) {
            setFile(acceptedFiles[0]);
        }

    }, []);

    const { getRootProps, getInputProps, isDragActive } =
        useDropzone({

            accept: {
                "application/pdf": [".pdf"],
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
            },

            multiple: false,

            onDrop,

        });

    async function handleUpload() {

        if (!file) {

            toast.error("Please select a resume.");

            return;

        }

        setLoading(true);

        const formData = new FormData();

        formData.append("resume", file);

        try {

            const response = await api.post(
                "/upload",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            toast.success(response.data.message);

            setFile(null);

        } catch (error) {

            toast.error(
                error.response?.data?.message ||
                "Upload failed."
            );

        } finally {

            setLoading(false);

        }

    }

    return (

        <MainLayout>

            <Typography
                variant="h4"
                gutterBottom
            >
                Upload Resume
            </Typography>

            <Paper
                {...getRootProps()}
                sx={{
                    border: "2px dashed #1976d2",
                    borderRadius: 3,
                    p: 5,
                    textAlign: "center",
                    cursor: "pointer",
                    backgroundColor: isDragActive
                        ? "#f0f8ff"
                        : "#fafafa",
                }}
            >

                <input {...getInputProps()} />

                <Typography variant="h6">

                    {isDragActive
                        ? "Drop your resume here..."
                        : "Drag & Drop Resume Here"}

                </Typography>

                <Typography sx={{ mt: 1 }}>
                    PDF or DOCX
                </Typography>

            </Paper>

            {file && (

                <Box mt={3}>

                    <Typography>

                        Selected File:

                        {" "}

                        <strong>{file.name}</strong>

                    </Typography>

                </Box>

            )}

            <Button

                sx={{ mt: 3 }}

                variant="contained"

                onClick={handleUpload}

                disabled={loading}

            >

                {loading ? (
                    <CircularProgress
                        size={24}
                        color="inherit"
                    />
                ) : (
                    "Upload Resume"
                )}

            </Button>

        </MainLayout>

    );

}