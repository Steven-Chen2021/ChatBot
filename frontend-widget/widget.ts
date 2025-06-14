import { LitElement, html, css } from 'lit';

interface Message {
  sender: 'user' | 'bot';
  text: string;
}

export class ChatBotWidget extends LitElement {
  static styles = css`
    :host {
      position: fixed;
      bottom: 20px;
      right: 20px;
      font-family: Arial, sans-serif;
      z-index: 9999;
    }

    .chat-toggle {
      padding: 8px 12px;
      background: #6200ee;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    .chat-window {
      width: 320px;
      height: 420px;
      border: 1px solid #ccc;
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      background: #fff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }

    .header {
      background: #6200ee;
      color: #fff;
      padding: 8px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top-left-radius: 8px;
      border-top-right-radius: 8px;
    }

    .header button {
      background: transparent;
      border: none;
      color: #fff;
      cursor: pointer;
    }

    .messages {
      flex: 1;
      padding: 8px;
      overflow-y: auto;
      background: #fafafa;
    }

    .message {
      margin-bottom: 8px;
      display: flex;
    }

    .message.user {
      justify-content: flex-end;
    }

    .bubble {
      max-width: 80%;
      padding: 6px 10px;
      border-radius: 12px;
    }

    .user .bubble {
      background: #e0e0e0;
    }

    .bot .bubble {
      background: #6200ee;
      color: white;
    }

    form {
      display: flex;
      border-top: 1px solid #ccc;
    }

    input[type='text'] {
      flex: 1;
      padding: 8px;
      border: none;
    }

    button.send {
      padding: 8px 12px;
      border: none;
      background: #6200ee;
      color: white;
      cursor: pointer;
    }
  `;

  private isOpen = false;
  private messages: Message[] = [];
  private userInput = '';

  private toggleChat() {
    this.isOpen = !this.isOpen;
    this.requestUpdate();
  }

  private handleInput(e: Event) {
    const target = e.target as HTMLInputElement;
    this.userInput = target.value;
  }

  private async sendMessage(e: Event) {
    e.preventDefault();
    const text = this.userInput.trim();
    if (!text) return;

    // Add user message
    this.messages = [...this.messages, { sender: 'user', text }];
    this.userInput = '';
    this.requestUpdate();

    try {
      const res = await fetch('/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      })
      const data = await res.json()
      this.messages = [...this.messages, { sender: 'bot', text: data.response }]
    } catch {
      this.messages = [...this.messages, { sender: 'bot', text: 'Error' }]
    }
    this.requestUpdate()
  }

  render() {
    return html`
      <button class="chat-toggle" @click=${this.toggleChat}>
        ${this.isOpen ? 'Minimize' : 'Open'} Chat
      </button>
      ${this.isOpen
        ? html`
            <div class="chat-window">
              <div class="header">
                <span>ChatBot</span>
                <button @click=${this.toggleChat}>✕</button>
              </div>
              <div class="messages">
                ${this.messages.map(
                  (m) => html`
                    <div class="message ${m.sender}">
                      <div class="bubble">${m.text}</div>
                    </div>
                  `
                )}
              </div>
              <form @submit=${this.sendMessage}>
                <input
                  type="text"
                  .value=${this.userInput}
                  @input=${this.handleInput}
                  placeholder="Type a message..."
                />
                <button class="send" type="submit">Send</button>
              </form>
            </div>
          `
        : ''}
    `;
  }
}