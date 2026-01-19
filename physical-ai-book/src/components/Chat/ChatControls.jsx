import React from 'react';

const ChatControls = ({
  topK,
  setTopK,
  mode,
  setMode,
  selectedText,
  setSelectedText,
  modeEnabled
}) => {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      gap: '16px',
      padding: '16px 0',
      width: '100%'
    }}>
      <div style={{
        display: 'flex',
        gap: '20px',
        alignItems: 'center',
        flexWrap: 'wrap',
        padding: '4px 0'
      }}>
        {/* Top K Selector */}
        <div style={{ flex: '0 0 auto' }}>
          <label htmlFor="top-k-selector" style={{
            display: 'block',
            fontSize: '13px',
            fontWeight: '500',
            color: '#64748b',
            marginBottom: '8px',
            textTransform: 'uppercase',
            letterSpacing: '0.5px'
          }}>
            Results
          </label>
          <div style={{
            position: 'relative'
          }}>
            <select
              id="top-k-selector"
              value={topK}
              onChange={(e) => setTopK(Number(e.target.value))}
              style={{
                padding: '10px 36px 10px 14px',
                border: '1px solid #e2e8f0',
                borderRadius: '20px',
                fontSize: '14px',
                backgroundColor: '#ffffff',
                color: '#1e293b',
                appearance: 'none',
                cursor: 'pointer',
                minWidth: '90px',
                boxShadow: '0 1px 2px rgba(0, 0, 0, 0.05)',
                transition: 'border-color 0.2s ease, box-shadow 0.2s ease'
              }}
              onFocus={(e) => {
                e.target.style.borderColor = '#94a3b8';
                e.target.style.boxShadow = '0 0 0 3px rgba(59, 130, 246, 0.1)';
              }}
              onBlur={(e) => {
                e.target.style.borderColor = '#e2e8f0';
                e.target.style.boxShadow = '0 1px 2px rgba(0, 0, 0, 0.05)';
              }}
            >
              {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(num => (
                <option key={num} value={num}>{num}</option>
              ))}
            </select>
            <div style={{
              position: 'absolute',
              right: '12px',
              top: '50%',
              transform: 'translateY(-50%)',
              pointerEvents: 'none',
              color: '#64748b',
              fontSize: '12px'
            }}>
              ▼
            </div>
          </div>
        </div>

        {/* Mode Toggle */}
        <div style={{ flex: '0 0 auto' }}>
          <label htmlFor="mode-toggle" style={{
            display: 'block',
            fontSize: '13px',
            fontWeight: '500',
            color: '#64748b',
            marginBottom: '8px',
            textTransform: 'uppercase',
            letterSpacing: '0.5px'
          }}>
            Mode
          </label>
          <div style={{
            display: 'flex',
            border: '1px solid #e2e8f0',
            borderRadius: '20px',
            overflow: 'hidden',
            backgroundColor: '#f8fafc',
            boxShadow: '0 1px 2px rgba(0, 0, 0, 0.05)'
          }}>
            <button
              type="button"
              onClick={() => setMode('retrieval')}
              style={{
                padding: '10px 20px',
                border: 'none',
                backgroundColor: mode === 'retrieval' ? '#3b82f6' : 'transparent',
                color: mode === 'retrieval' ? 'white' : '#64748b',
                fontSize: '14px',
                fontWeight: mode === 'retrieval' ? '600' : '500',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                minWidth: '100px'
              }}
            >
              Retrieval
            </button>
            <button
              type="button"
              onClick={() => setMode('selected-text-only')}
              style={{
                padding: '10px 20px',
                border: 'none',
                backgroundColor: mode === 'selected-text-only' ? '#3b82f6' : 'transparent',
                color: mode === 'selected-text-only' ? 'white' : '#64748b',
                fontSize: '14px',
                fontWeight: mode === 'selected-text-only' ? '600' : '500',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                minWidth: '130px'
              }}
            >
              Selected Text
            </button>
          </div>
        </div>
      </div>

      {/* Selected Text Input (only shown when mode is selected-text-only) */}
      {modeEnabled && (
        <div style={{
          marginTop: '8px',
          padding: '18px',
          backgroundColor: '#f8fafc',
          border: '1px solid #e2e8f0',
          borderRadius: '16px',
          boxShadow: '0 1px 3px rgba(0, 0, 0, 0.05)'
        }}>
          <div style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: '12px'
          }}>
            <label htmlFor="selected-text-input" style={{
              fontSize: '14px',
              fontWeight: '600',
              color: '#1e293b',
              display: 'flex',
              alignItems: 'center',
              gap: '10px'
            }}>
              <span style={{
                fontSize: '16px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                width: '24px',
                height: '24px',
                borderRadius: '6px',
                backgroundColor: '#dbeafe',
                color: '#1d4ed8'
              }}>
                📝
              </span>
              Context Text
            </label>
            <span style={{
              fontSize: '12px',
              color: '#64748b',
              backgroundColor: '#e2e8f0',
              padding: '4px 10px',
              borderRadius: '14px',
              fontWeight: '500'
            }}>
              Required
            </span>
          </div>
          <textarea
            id="selected-text-input"
            value={selectedText}
            onChange={(e) => setSelectedText(e.target.value)}
            placeholder="Paste the selected text you want to discuss..."
            style={{
              width: '100%',
              minHeight: '90px',
              padding: '14px',
              border: '1px solid #cbd5e1',
              borderRadius: '12px',
              fontSize: '14px',
              lineHeight: '1.5',
              resize: 'vertical',
              outline: 'none',
              backgroundColor: '#ffffff',
              boxShadow: '0 1px 2px rgba(0, 0, 0, 0.05)',
              transition: 'border-color 0.2s ease, box-shadow 0.2s ease'
            }}
            onFocus={(e) => {
              e.target.style.borderColor = '#94a3b8';
              e.target.style.boxShadow = '0 0 0 3px rgba(59, 130, 246, 0.1)';
            }}
            onBlur={(e) => {
              e.target.style.borderColor = '#cbd5e1';
              e.target.style.boxShadow = '0 1px 2px rgba(0, 0, 0, 0.05)';
            }}
          />
          <div style={{
            fontSize: '13px',
            color: '#64748b',
            marginTop: '10px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            padding: '8px 0',
            borderTop: '1px solid #e2e8f0'
          }}>
            <span style={{ fontSize: '16px' }}>💡</span>
            <span>This text will be used as context for your query</span>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatControls;