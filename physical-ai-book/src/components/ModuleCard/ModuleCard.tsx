import React from 'react';
import Link from '@docusaurus/Link';
import clsx from 'clsx';
import styles from './styles.module.css';

interface ModuleCardProps {
  title: string;
  description: string;
  icon?: React.ReactNode;
  to: string;
  number: string;
  className?: string;
}

export default function ModuleCard({
  title,
  description,
  icon,
  to,
  number,
  className,
}: ModuleCardProps): JSX.Element {
  // Generate a unique color based on the module number for visual differentiation
  const getModuleColor = (num: string) => {
    const colors = [
      'linear-gradient(135deg, #0ea5e9, #38bdf8)',  // Blue for module 1
      'linear-gradient(135deg, #8b5cf6, #a78bfa)',  // Purple for module 2
      'linear-gradient(135deg, #06b6d4, #22d3ee)',  // Cyan for module 3
      'linear-gradient(135deg, #84cc16, #a3e635)',  // Lime for module 4
    ];
    const index = parseInt(num) - 1;
    return colors[index] || colors[0];
  };

  const moduleGradient = getModuleColor(number);

  return (
    <Link to={to} className={clsx('card', styles.moduleCard, className)}>
      <div className={styles.cardHeader}>
        <div
          className={styles.moduleNumber}
          style={{ background: moduleGradient }}
        >
          {number}
        </div>
        <div className={styles.cardIcon}>
          {icon || (
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M2 17L12 22L22 17" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M2 12L12 17L22 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          )}
        </div>
      </div>
      <div className={styles.cardContent}>
        <h3 className={styles.cardTitle}>{title}</h3>
        <p className={styles.cardDescription}>{description}</p>
      </div>
      <div className={styles.cardFooter}>
        <span className={styles.learnMore}>Explore →</span>
      </div>
    </Link>
  );
}