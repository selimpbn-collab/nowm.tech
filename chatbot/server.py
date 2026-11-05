#!/usr/bin/env python3
"""
Hermes Dashboard Chatbot
Connects the dashboard chat widget to the Hermes agent via Telegram API.
"""
import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

# Configuration
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '9048657537:***')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '1068536256')
BASE_URL = os.environ.get('BASE_URL', 'https://selimpbn-collab.github.io/nowm.tech')

class ChatHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'ok', 'service': 'hermes-chatbot'}).encode())
        elif self.path == '/':
            self.serve_chat_widget()
    
    def serve_chat_widget(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hermes Chat - nowm.tech</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .font-mono { font-family: 'Fira Code', monospace; }
        .glass { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.3); }
        .dark .glass { background: rgba(15, 23, 42, 0.75); border: 1px solid rgba(255, 255, 255, 0.08); }
        .glow { box-shadow: 0 0 25px -5px rgba(20, 184, 166, 0.3); }
        .dark .glow { box-shadow: 0 0 25px -5px rgba(56, 189, 248, 0.2); }
    </style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 min-h-screen">
    <div class="fixed bottom-5 right-5 z-50">
        <div class="chat-widget" id="chatWidget">
            <div class="chat-header glass rounded-2xl p-3">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-brand-600 via-brand-500 to-cyan-400 flex items-center justify-center text-white font-bold">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold">Hermes Assistant</h4>
                        <p class="text-xs text-slate-500">Online - I'm your trading assistant</p>
                    </div>
                    <button onclick="closeChat()" class="text-slate-400 hover:text-slate-600">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
            </div>
            <div class="chat-messages glass rounded-xl p-4 max-h-96 overflow-y-auto" id="chatMessages">
                <div class="text-center text-sm text-slate-500 mb-4">
                    <i class="fas fa-comments mr-2"></i>
                    Ask me anything about trading, EAs, or your website!
                </div>
            </div>
            <div class="chat-input glass rounded-xl p-3">
                <div class="flex gap-2">
                    <input type="text" id="chatInput" class="flex-1 px-4 py-2 rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-sm focus:outline-none focus:border-brand-500" placeholder="Type your message...">
                    <button onclick="sendMessage()" class="px-4 py-2 bg-brand-500 text-white rounded-xl hover:bg-brand-400 transition-all">
                        <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <script>
        let messages = [];
        const chatWidget = document.getElementById('chatWidget');
        const chatMessages = document.getElementById('chatMessages');
        const chatInput = document.getElementById('chatInput');

        // Open chat
        function openChat() {
            chatWidget.style.display = 'block';
            chatWidget.classList.add('open');
            scrollToBottom();
        }

        function closeChat() {
            chatWidget.style.display = 'none';
            chatWidget.classList.remove('open');
            chatInput.value = '';
        }

        function scrollToBottom() {
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function addMessage(text, type) {
            const div = document.createElement('div');
            div.className = 'mb-3 ' + (type === 'bot' ? 'text-right' : 'text-left');
            div.innerHTML = '<div class="flex ' + (type === 'bot' ? 'justify-end' : 'justify-start') + '"><div class="max-w-[80%] ' + (type === 'bot' ? 'bg-brand-500/10 text-brand-600' : 'bg-slate-500/10 text-slate-600') + ' rounded-2xl px-4 py-2 text-sm">' + text + '</div></div>';
            chatMessages.appendChild(div);
            scrollToBottom();
        }

        async function sendMessage() {
            const text = chatInput.value.trim();
            if (!text) return;

            chatInput.value = '';
            addMessage(text, 'user');

            // Show typing indicator
            const typingDiv = document.createElement('div');
            typingDiv.className = 'flex justify-end';
            typingDiv.innerHTML = '<div class="text-xs text-slate-500"><i class="fas fa-spinner fa-spin"></i></div>';
            chatMessages.appendChild(typingDiv);
            scrollToBottom();

            // Send to backend
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ message: text })
                });
                const data = await response.json();
                typingDiv.remove();
                if (data.response) {
                    addMessage(data.response, 'bot');
                } else {
                    addMessage('Sorry, I couldn\'t process that request.', 'bot');
                }
            } catch (error) {
                typingDiv.remove();
                addMessage('Error: ' + error.message, 'bot');
            }
        }

        // Send on Enter
        chatInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                sendMessage();
            }
        });

        // Auto-open chat on page load (optional)
        // window.addEventListener('load', openChat);
    </script>
</body>
</html>"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)
            message = data.get('message', '')

            # Use Hermes AI agent via Nous inference API
            import urllib.request
            import json as json_lib

            hermes_payload = {
                "model": "upstage/solar-mini4:free",
                "messages": [
                    {"role": "user", "content": message}
                ],
                "max_tokens": 500,
                "temperature": 0.7
            }

            hermes_url = "https://inference-api.nousresearch.com/v1/chat/completions"
            hermes_headers = {
                "Content-Type": "application/json"
            }

            try:
                import os
                api_key = os.environ.get('NOUS_API_KEY', '')
                if api_key:
                    hermes_headers['Authorization'] = f'Bearer {api_key}'

                hermes_data = json_lib.dumps(hermes_payload).encode('utf-8')
                hermes_request = urllib.request.Request(
                    hermes_url,
                    data=hermes_data,
                    headers=hermes_headers,
                    method='POST'
                )

                with urllib.request.urlopen(hermes_request, timeout=30) as response:
                    hermes_result = json_lib.loads(response.read().decode())
                    if 'choices' in hermes_result and len(hermes_result['choices']) > 0:
                        response_text = hermes_result['choices'][0]['message']['content']
                    else:
                        response_text = "I received your message but the AI response is unavailable."

            except Exception as e:
                response_text = "I received your message but the AI response is unavailable."

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'response': response_text,
                'status': 'ok',
                'source': 'hermes'
            }).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run_server(port=8000):
    server = HTTPServer(('', port), ChatHandler)
    print(f'Chat server running on port {port}')
    print(f'Webhook: http://localhost:{port}/')
    server.serve_forever()

if __name__ == '__main__':
    run_server()
