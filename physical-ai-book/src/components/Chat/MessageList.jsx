import React from 'react';
import SourceDisplay from './SourceDisplay';

const MessageList = ({ messages }) => {
  return (
    <div style={{
      marginBottom: '15px',
      display: 'flex',
      flexDirection: 'column',
      gap: '24px'
    }}>
      {messages.length === 0 ? (
        <div style={{
          textAlign: 'center',
          padding: '60px 32px',
          color: '#475569',
          fontStyle: 'normal',
          fontSize: '19px',
          fontWeight: '600',
          backgroundColor: 'linear-gradient(135deg, #f8fafc, #f1f5f9)',
          borderRadius: '24px',
          border: '2px dashed #e2e8f0',
          margin: '32px 0',
          backdropFilter: 'blur(10px)'
        }}>
          <div style={{
            fontSize: '40px',
            marginBottom: '12px',
            opacity: '0.6'
          }}>
            💬
          </div>
          Start a conversation by asking a question about the book content...
        </div>
      ) : (
        messages.map((message) => (
          <div
            key={message.id}
            style={{
              display: 'flex',
              justifyContent: message.sender === 'user' ? 'flex-end' : 'flex-start',
              width: '100%'
            }}
          >
            <div
              style={{
                maxWidth: '100%',
                padding: '28px 32px',
                borderRadius: message.sender === 'user'
                  ? '32px 32px 4px 32px'
                  : '32px 32px 32px 4px',
                backgroundColor: message.sender === 'user'
                  ? 'linear-gradient(135deg, #3b82f6, #1d4ed8)'
                  : message.sender === 'system'
                  ? 'linear-gradient(135deg, #ef4444, #dc2626)'
                  : 'linear-gradient(135deg, #ffffff, #f8fafc)',
                color: message.sender === 'user'
                  ? 'white'
                  : message.sender === 'system'
                  ? 'white'
                  : '#1e293b',
                wordWrap: 'break-word',
                boxShadow: '0 10px 20px -4px rgba(0, 0, 0, 0.12), 0 8px 12px -4px rgba(0, 0, 0, 0.08)',
                border: message.sender !== 'user' && message.sender !== 'system' ? '1px solid #e2e8f0' : 'none',
                position: 'relative',
                transition: 'transform 0.2s ease, box-shadow 0.2s ease',
                backdropFilter: 'blur(10px)'
              }}
              onMouseEnter={(e) => {
                if (message.sender !== 'user' && message.sender !== 'system') {
                  e.target.style.transform = 'translateY(-1px)';
                  e.target.style.boxShadow = '0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.01)';
                }
              }}
              onMouseLeave={(e) => {
                if (message.sender !== 'user' && message.sender !== 'system') {
                  e.target.style.transform = 'translateY(0)';
                  e.target.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03)';
                }
              }}
            >
              <div style={{
                fontWeight: '700',
                marginBottom: '12px',
                fontSize: '15px',
                display: 'flex',
                alignItems: 'center',
                gap: '10px'
              }}>
                {message.sender === 'user' ? (
                  <>
                    <span style={{fontSize: '16px'}}>👤</span>
                    <span>You</span>
                  </>
                ) : message.sender === 'system' ? (
                  <>
                    <span style={{fontSize: '16px'}}>⚠️</span>
                    <span>System</span>
                  </>
                ) : (
                  <>
                    <span style={{fontSize: '16px'}}>🤖</span>
                    <span>Assistant</span>
                  </>
                )}
              </div>
              <div style={{
                whiteSpace: 'pre-wrap',
                lineHeight: '1.9',
                fontSize: '17px',
                fontWeight: '500',
                letterSpacing: '0.4px',
                color: '#1e293b',
                marginTop: '8px'
              }}>
                {message.text}
              </div>

              {/* Show sources if this is an assistant message with sources */}
              {message.sender === 'assistant' && message.sources && message.sources.length > 0 && (
                <div style={{ marginTop: '16px' }}>
                  <SourceDisplay sources={message.sources} modeUsed={message.modeUsed} />
                </div>
              )}

              {message.sender === 'assistant' && message.sources && message.sources.length === 0 && message.modeUsed === 'retrieval' && (
                <div style={{
                  marginTop: '20px',
                  padding: '20px',
                  backgroundColor: '#fef9c3',
                  border: '1px solid #fbbf24',
                  borderRadius: '16px',
                  color: '#92400e',
                  fontSize: '16px',
                  fontWeight: '500'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span>🔍</span>
                    <span><strong>Info:</strong> No sources found for this query. The response is generated based on the model's training.</span>
                  </div>
                </div>
              )}
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default MessageList;