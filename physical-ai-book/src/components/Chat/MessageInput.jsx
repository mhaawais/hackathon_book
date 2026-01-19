import React, { useState, useRef } from 'react';

const MessageInput = ({ onSubmit, isLoading }) => {
  const [inputValue, setInputValue] = useState('');
  const textareaRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim() && !isLoading) {
      onSubmit(inputValue);
      setInputValue('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ width: '100%' }}>
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        gap: '12px'
      }}>
        <div style={{
          display: 'flex',
          gap: '12px',
          alignItems: 'flex-end',
          width: '100%'
        }}>
          <div style={{ flex: 1, position: 'relative' }}>
            <textarea
              ref={textareaRef}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask a question about the book content..."
              disabled={isLoading}
              style={{
                width: '100%',
                minHeight: '56px',
                maxHeight: '120px',
                padding: '12px 45px 12px 16px',
                border: '1px solid #e2e8f0',
                borderRadius: '24px',
                resize: 'none',
                fontSize: '16px',
                lineHeight: '1.6',
                outline: 'none',
                backgroundColor: '#ffffff',
                color: '#1e293b',
                boxShadow: '0 2px 4px rgba(0, 0, 0, 0.08)',
                transition: 'border-color 0.2s ease, box-shadow 0.2s ease',
                fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
              }}
              onFocus={(e) => {
                e.target.style.borderColor = '#94a3b8';
                e.target.style.boxShadow = '0 0 0 3px rgba(59, 130, 246, 0.1)';
              }}
              onBlur={(e) => {
                e.target.style.borderColor = '#e2e8f0';
                e.target.style.boxShadow = '0 1px 2px rgba(0, 0, 0, 0.05)';
              }}
            />
            <div style={{
              position: 'absolute',
              right: '12px',
              top: '50%',
              transform: 'translateY(-50%)',
              display: 'flex',
              alignItems: 'center',
              gap: '4px'
            }}>
              <div style={{
                fontSize: '14px',
                color: '#64748b',
                padding: '4px 8px',
                borderRadius: '12px',
                backgroundColor: '#f1f5f9',
                display: isLoading ? 'inline-block' : 'none'
              }}>
                ...
              </div>
            </div>
          </div>
          <button
            type="submit"
            disabled={isLoading || !inputValue.trim()}
            style={{
              padding: '12px 20px',
              background: inputValue.trim() && !isLoading
                ? 'linear-gradient(135deg, #3b82f6, #1d4ed8)'
                : 'linear-gradient(135deg, #cbd5e1, #9ca3af)',
              color: 'white',
              border: 'none',
              borderRadius: '20px',
              cursor: inputValue.trim() && !isLoading ? 'pointer' : 'not-allowed',
              fontSize: '13px',
              fontWeight: '500',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              transition: 'all 0.2s ease',
              boxShadow: '0 4px 6px -1px rgba(59, 130, 246, 0.2), 0 2px 4px -2px rgba(59, 130, 246, 0.2)',
              position: 'relative',
              overflow: 'hidden'
            }}
            onMouseDown={(e) => {
              if (inputValue.trim() && !isLoading) {
                e.currentTarget.style.transform = 'scale(0.98)';
              }
            }}
            onMouseUp={(e) => {
              if (inputValue.trim() && !isLoading) {
                e.currentTarget.style.transform = 'scale(1)';
              }
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = 'scale(1)';
            }}
          >
            {isLoading ? (
              <>
                <div style={{
                  width: '16px',
                  height: '16px',
                  borderTop: '2px solid white',
                  borderRight: '2px solid transparent',
                  borderRadius: '50%',
                  animation: 'spin 1s linear infinite'
                }}></div>
                Sending...
              </>
            ) : (
              <>
                <span style={{ fontSize: '16px' }}>➤</span> Send
              </>
            )}
          </button>
        </div>

        {isLoading && (
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            color: '#64748b',
            fontSize: '14px',
            padding: '8px 12px',
            backgroundColor: '#f8fafc',
            borderRadius: '12px',
            marginLeft: 'auto',
            marginRight: 'auto',
            width: 'fit-content'
          }}>
            <div style={{
              width: '16px',
              height: '16px',
              borderTop: '2px solid #3b82f6',
              borderRight: '2px solid transparent',
              borderRadius: '50%',
              animation: 'spin 1s linear infinite'
            }}></div>
            <span>AI is thinking...</span>
          </div>
        )}
      </div>

      <style jsx>{`
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </form>
  );
};

export default MessageInput;