import { LitElement, html, css } from 'lit';

export class ChatBotWidget extends LitElement {
  static styles = css`
    /* Add styles for light/dark mode and toggle button */
  `;

  private isOpen = false;

  toggleChat() {
    this.isOpen = !this.isOpen;
    this.requestUpdate();
  }

  render() {
    return html`
      <button @click="${this.toggleChat}">
        ${this.isOpen ? 'Minimize' : 'Open'} Chat
      </button>
      ${this.isOpen
        ? html`<div class="chat-interface">Chat interface here</div>`
        : ''}
    `;
  }
}