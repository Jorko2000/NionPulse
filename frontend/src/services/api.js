import axios from "axios";
const API_BASE = "http://localhost:8000";
export const fetchEvents = async () => (await axios.get(`${API_BASE}/events`)).data;
export const fetchMetrics = async () => (await axios.get(`${API_BASE}/metrics`)).data;
