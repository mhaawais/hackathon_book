import React, { useState } from 'react';
import clsx from 'clsx';
import styles from './FloatingChat.module.css';
import ChatWindow from './Chat/ChatWindow';

const FloatingChat = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const closeChat = () => {
    setIsOpen(false);
  };

  return (
    <>
      <button
        className={clsx(styles.floatingChatButton, {
          [styles.isOpen]: isOpen
        })}
        onClick={toggleChat}
        aria-label={isOpen ? "Close chat" : "Open chat"}
        title={isOpen ? "Close chat" : "Chat with AI Assistant"}
        style={{
          position: 'fixed',
          bottom: isOpen ? '330px' : '30px',
          right: '30px',
          zIndex: 1000,
          width: '60px',
          height: '60px',
          borderRadius: '50%',
          border: 'none',
          background: 'var(--ifm-color-primary)',
          color: 'white',
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
          transition: 'all 0.3s ease, bottom 0.3s ease'
        }}
      >
        <div className={styles.chatIcon}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            style={{ width: '24px', height: '24px' }}
          >
            {isOpen ? (
              // X icon when open
              <path d="M18 6 6 18M6 6l12 12" />
            ) : (
              // Chat bubble icon when closed
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
            )}
          </svg>
        </div>
        {!isOpen && (
          <span className={styles.chatBadge}>
            <span className={styles.pulse}></span>
          </span>
        )}
      </button>

      {isOpen && (
        <div
          className={styles.chatPopupOverlay}
          onClick={closeChat}
          style={{
            position: 'fixed',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundColor: 'rgba(0, 0, 0, 0.5)',
            zIndex: 999,
            display: 'flex',
            alignItems: 'flex-end',
            justifyContent: 'flex-end',
            padding: '20px',
            backdropFilter: 'blur(4px)'
          }}
        >
          <div
            className={styles.chatPopup}
            onClick={(e) => e.stopPropagation()}
            style={{
              width: '400px',
              height: '500px',
              maxHeight: '80vh',
              backgroundColor: '#ffffff',
              borderRadius: '24px',
              overflow: 'hidden',
              display: 'flex',
              flexDirection: 'column',
              boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(0, 0, 0, 0.05)',
              animation: 'slideIn 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
              border: '1px solid rgba(255, 255, 255, 0.2)',
              backdropFilter: 'blur(10px)',
              fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif'
            }}
          >
            <div style={{
              padding: '20px 24px',
              background: 'linear-gradient(135deg, var(--ifm-color-primary), #6366f1)',
              color: 'white',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              borderBottom: '1px solid rgba(255, 255, 255, 0.1)'
            }}>
              <div style={{
                display: 'flex',
                alignItems: 'center',
                gap: '10px'
              }}>
                <div style={{
                  width: '8px',
                  height: '8px',
                  borderRadius: '50%',
                  backgroundColor: '#10b981',
                  boxShadow: '0 0 8px rgba(16, 185, 129, 0.5)'
                }}></div>
                <h3 style={{
                  margin: 0,
                  fontSize: '16px',
                  fontWeight: '600',
                  letterSpacing: '-0.1px'
                }}>
                  AI Assistant
                </h3>
              </div>
              <button
                onClick={closeChat}
                style={{
                  background: 'rgba(255, 255, 255, 0.1)',
                  border: 'none',
                  color: 'white',
                  fontSize: '18px',
                  cursor: 'pointer',
                  padding: '6px',
                  borderRadius: '50%',
                  width: '32px',
                  height: '32px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  transition: 'background-color 0.2s ease',
                  backdropFilter: 'blur(10px)'
                }}
                onMouseEnter={(e) => {
                  e.target.style.backgroundColor = 'rgba(255, 255, 255, 0.2)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.backgroundColor = 'rgba(255, 255, 255, 0.1)';
                }}
              >
                ×
              </button>
            </div>
            <div style={{
              flex: 1,
              overflow: 'hidden',
              backgroundColor: '#fafbfc'
            }}>
              <ChatWindow />
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default FloatingChat;