#!/bin/bash
# Hermes Chat Bot Startup Script
# Run this to start the chat server

cd /opt/data/nowm.tech/chatbot
echo "Starting Hermes Chat Bot..."
echo "Webhook: http://localhost:8000/"
echo "Press Ctrl+C to stop"
python3 server.py
