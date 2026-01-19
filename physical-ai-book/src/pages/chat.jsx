import React from 'react';
import ChatWindow from '../components/Chat/ChatWindow';

const ChatPage = () => {
  return (
    <div style={{
      minHeight: '100vh',
      padding: '20px 10px',
      background: 'linear-gradient(135deg, #f0f9ff, #e0f2fe)',
    }}>
      <div className="container">
        <div className="row">
          <div className="col col--12">
            <div style={{
              maxWidth: '1200px',
              margin: '0 auto',
              height: '80vh',
              padding: '10px'
            }}>
              <ChatWindow />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatPage;