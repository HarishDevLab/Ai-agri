# AI-Based Farmer Query Support and Advisory System

## Overview
This project is an **AI-powered advisory system** designed to help farmers get instant, personalized guidance for crop management, pest control, weather insights, government schemes, and more. The system supports **voice, text, and image inputs** in Malayalam, processes the information using AI models, and provides tailored responses to each farmer.

---

## Features

### 1. Multimodal Query Handling
- **Voice Input**: Farmers can speak in Malayalam; converted to text using **OpenAI Whisper**.
- **Text Input**: Farmers can type queries in Malayalam or English.
- **Image Input**: Farmers can upload photos of crops or leaves for disease/pest detection.

### 2. Image Processing
- Uses **YOLOv8** for detection and classification of crop diseases and pests.
- Preprocessing with **OpenCV**: image resizing, cropping, noise reduction, leaf segmentation.
- Outputs a **structured report** (disease/pest type, affected area, confidence score) for LLM processing.

### 3. AI-Powered Knowledge Engine
- **Main LLM**: Open-source **LLaMA 3 (8B)** fine-tuned with agriculture datasets.
- Processes text queries and image AI reports to provide **personalized advice**.
- Supports **translation workflow**:
  - Malayalam → English → LLM → English → Malayalam
- Uses **farmer-specific factors**: location, soil type, crop details, irrigation, past issues, etc.

### 4. Context Awareness
- Personalized advice based on:
  - Crop type, growth stage, season
  - Farmer location and soil data
  - Weather and local advisories
  - Government schemes

### 5. Escalation System
- If AI confidence is low, queries are escalated to **local agriculture officers**.
- Ensures **all farmers receive answers**, either AI-generated or from experts.

### 6. Learning Loop
- Collects **real queries and farmer feedback**.
- Stores data in a **feedback database** for:
  - Periodic fine-tuning of LLM
  - Continuous improvement of responses
  - Incorporation of local expert knowledge

### 7. Weather, Pest, and Government Scheme Updates
- System can be updated **via APIs** or manually by administrators.
- Ensures **advice remains current** with crop calendars, pest outbreaks, and government schemes.

---

## Architecture & Workflow

### 1. Input
- Farmer provides:
  - **Voice** → Whisper converts to text
  - **Text** → Direct input or translation
  - **Image** → Uploaded crop/leaf photo

### 2. Image Processing
- Preprocess image (OpenCV)
- Detect and classify diseases/pests using YOLOv8
- Generate structured report (disease, affected area, confidence)

### 3. LLM Processing
- Text queries + structured image report + farmer factors → LLaMA 3 (8B)
- LLM generates **tailored advisory** in English
- Translate response → Malayalam (for farmer comprehension)

### 4. Output
- Advisory delivered as:
  - **Text** in Malayalam
  - **Audio** (Text-to-Speech) for illiterate farmers (if needed)

### 5. Escalation & Feedback
- Low confidence queries → flagged to agriculture officers
- Farmer feedback stored for **continuous learning and system improvement**

---

## Tech Stack (Not Yet Finalised)

### Backend
- **Node.js** (API endpoints, backend logic)
- **Python** (AI processing)
  - OpenAI Whisper (voice-to-text)
  - PyTorch / YOLOv8 (image processing)
  - LLaMA 3 (8B) fine-tuned (text advisory)
  - Translation: IndicTrans2 or Google Translate fallback
  - For Later stage: gTTS or Coqui TTS (text-to-speech)

### Frontend
- Web interface or mobile-friendly UI (prototype phase)
- Input forms for text, voice, and image upload
- Display advisory output and optional audio playback

### Database
- MongoDB / PostgreSQL for:
  - Farmer profiles and factors
  - Query and feedback storage
  - Historical advisory data

---

## Deployment (Not Yet Finalised)
- **Prototype phase**: Google Colab for AI model inference
- **Backend**: Node.js server (for integration with frontend)
- **Frontend**: Web or mobile app
- **Deployment status**: Not yet finalized
- Future production may use cloud hosting (GCP, AWS) or dedicated servers
