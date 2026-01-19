import React, { useState } from 'react';

const SourceDisplay = ({ sources, modeUsed }) => {
  const [expandedSources, setExpandedSources] = useState({});

  const toggleSource = (index) => {
    setExpandedSources(prev => ({
      ...prev,
      [index]: !prev[index]
    }));
  };

  return (
    <div style={{
      marginTop: '10px',
      padding: '10px',
      backgroundColor: '#e9ecef',
      borderRadius: '4px',
      border: '1px solid #ced4da'
    }}>
      <div style={{ fontWeight: 'bold', marginBottom: '8px', fontSize: '14px' }}>
        Sources ({sources.length})
      </div>

      {sources.length === 0 ? (
        <div style={{ fontStyle: 'italic', color: '#6c757d' }}>
          No sources available for this response.
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {sources.map((source, index) => (
            <div key={index} style={{
              padding: '8px',
              backgroundColor: 'white',
              border: '1px solid #dee2e6',
              borderRadius: '4px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                <a
                  href={source.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  style={{
                    fontWeight: '600',
                    color: '#3b82f6',
                    textDecoration: 'none',
                    fontSize: '13px',
                    flex: 1,
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    whiteSpace: 'nowrap'
                  }}
                >
                  {source.url ? new URL(source.url).hostname : 'Source Link'}
                </a>
                <span style={{
                  fontSize: '12px',
                  color: '#64748b',
                  backgroundColor: '#f1f5f9',
                  padding: '2px 8px',
                  borderRadius: '12px',
                  marginLeft: '8px',
                  flexShrink: 0
                }}>
                  {(source.score || 0).toFixed(4)}
                </span>
              </div>

              <div style={{ marginTop: '6px' }}>
                <button
                  onClick={() => toggleSource(index)}
                  style={{
                    background: 'none',
                    border: '1px solid #cbd5e1',
                    color: '#475569',
                    padding: '6px 12px',
                    borderRadius: '8px',
                    cursor: 'pointer',
                    fontSize: '12px',
                    fontWeight: '500',
                    transition: 'all 0.2s ease',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '4px'
                  }}
                  onMouseEnter={(e) => {
                    e.target.style.backgroundColor = '#f1f5f9';
                    e.target.style.borderColor = '#94a3b8';
                  }}
                  onMouseLeave={(e) => {
                    e.target.style.backgroundColor = 'transparent';
                    e.target.style.borderColor = '#cbd5e1';
                  }}
                >
                  {expandedSources[index] ? (
                    <>
                      <span>▲</span> Hide Content
                    </>
                  ) : (
                    <>
                      <span>▼</span> Show Content
                    </>
                  )}
                </button>

                {expandedSources[index] && (
                  <div style={{
                    marginTop: '8px',
                    padding: '12px',
                    backgroundColor: '#f8fafc',
                    border: '1px solid #e2e8f0',
                    borderRadius: '12px',
                    fontSize: '13px',
                    lineHeight: '1.5',
                    whiteSpace: 'pre-wrap',
                    overflowX: 'auto',
                    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif'
                  }}>
                    <div style={{
                      fontWeight: '600',
                      color: '#1e293b',
                      marginBottom: '6px',
                      fontSize: '12px',
                      textTransform: 'uppercase',
                      letterSpacing: '0.5px'
                    }}>
                      Content Preview:
                    </div>
                    {source.content}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      )}

      {modeUsed === 'retrieval' && sources.length === 0 && (
        <div style={{
          marginTop: '8px',
          padding: '8px',
          backgroundColor: '#fff3cd',
          border: '1px solid #ffeaa7',
          borderRadius: '4px',
          color: '#856404',
          fontSize: '12px'
        }}>
          ⚠️ No sources returned for this query. The response was generated without retrieval.
        </div>
      )}
    </div>
  );
};

export default SourceDisplay;