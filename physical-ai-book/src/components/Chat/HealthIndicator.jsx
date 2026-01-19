import React from 'react';

const HealthIndicator = ({ status }) => {
  const getStatusStyle = (status) => {
    switch (status?.status) {
      case 'healthy':
        return {
          color: '#059669', // emerald-600
          backgroundColor: '#ecfdf5', // emerald-50
          border: '1px solid #a7f3d0' // emerald-200
        };
      case 'degraded':
        return {
          color: '#d97706', // amber-600
          backgroundColor: '#fef3c7', // amber-100
          border: '1px solid #fde68a' // amber-200
        };
      case 'unhealthy':
        return {
          color: '#dc2626', // red-600
          backgroundColor: '#fef2f2', // red-50
          border: '1px solid #fecaca' // red-200
        };
      case 'checking':
        return {
          color: '#0284c7', // sky-600
          backgroundColor: '#f0f9ff', // sky-50
          border: '1px solid #bae6fd' // sky-200
        };
      default:
        return {
          color: '#64748b', // slate-500
          backgroundColor: '#f1f5f9', // slate-100
          border: '1px solid #cbd5e1' // slate-200
        };
    }
  };

  const getStatusText = (status) => {
    switch (status?.status) {
      case 'healthy':
        return 'Connected';
      case 'degraded':
        return 'Degraded';
      case 'unhealthy':
        return 'Unreachable';
      case 'checking':
        return 'Checking...';
      default:
        return 'Unknown';
    }
  };

  const statusStyle = getStatusStyle(status);

  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      padding: '6px 12px',
      borderRadius: '20px',
      ...statusStyle,
      fontSize: '12px',
      fontWeight: '600',
      backdropFilter: 'blur(10px)',
      boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
    }}>
      <div
        style={{
          width: '10px',
          height: '10px',
          borderRadius: '50%',
          backgroundColor: status?.status === 'healthy' ? '#059669' : // emerald-600
                         status?.status === 'degraded' ? '#d97706' : // amber-600
                         status?.status === 'unhealthy' ? '#dc2626' : // red-600
                         status?.status === 'checking' ? '#0284c7' : // sky-600
                         '#64748b', // slate-500
          animation: status?.status === 'checking' ? 'pulse 1.5s infinite' : 'none',
          boxShadow: status?.status === 'healthy' ? '0 0 8px rgba(5, 150, 105, 0.3)' :
                    status?.status === 'degraded' ? '0 0 8px rgba(217, 119, 6, 0.3)' :
                    status?.status === 'unhealthy' ? '0 0 8px rgba(220, 38, 38, 0.3)' :
                    status?.status === 'checking' ? '0 0 8px rgba(2, 132, 199, 0.3)' : 'none'
        }}
      ></div>
      <span style={{ letterSpacing: '0.2px' }}>{getStatusText(status)}</span>
    </div>
  );
};

export default HealthIndicator;