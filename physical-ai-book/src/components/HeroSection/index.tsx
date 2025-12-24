import React from 'react';
import Link from '@docusaurus/Link';
import clsx from 'clsx';
import styles from './styles.module.css';

interface HeroSectionProps {
  title: string;
  subtitle?: string;
  tagline?: string;
  ctaText?: string;
  ctaLink?: string;
  secondaryCtaText?: string;
  secondaryCtaLink?: string;
  className?: string;
}

export default function HeroSection({
  title,
  subtitle,
  tagline,
  ctaText = 'Get Started',
  ctaLink = '/docs/intro',
  secondaryCtaText,
  secondaryCtaLink,
  className,
}: HeroSectionProps): JSX.Element {
  return (
    <section className={clsx(styles.heroSection, className)}>
      <div className={styles.heroBackground}>
        <div className={styles.gridPattern}>
          <div className={styles.gridCell}></div>
          <div className={styles.gridCell}></div>
          <div className={styles.gridCell}></div>
          <div className={styles.gridCell}></div>
          <div className={styles.gridCell}></div>
          <div className={styles.gridCell}></div>
          <div className={styles.gridCell}></div>
          <div className={styles.gridCell}></div>
          <div className={styles.gridCell}></div>
        </div>
      </div>
      <div className={styles.heroContent}>
        <div className={styles.heroText}>
          {tagline && <div className={styles.heroTagline}>{tagline}</div>}
          <h1 className={styles.heroTitle}>{title}</h1>
          {subtitle && <p className={styles.heroSubtitle}>{subtitle}</p>}
          <div className={styles.heroButtons}>
            <Link className={clsx('button button--primary button--lg', styles.heroButton)} to={ctaLink}>
              {ctaText}
            </Link>
            {secondaryCtaText && secondaryCtaLink && (
              <Link className={clsx('button button--secondary button--lg', styles.heroButton, styles.heroButtonSecondary)} to={secondaryCtaLink}>
                {secondaryCtaText}
              </Link>
            )}
          </div>
        </div>
        <div className={styles.heroGraphic}>
          <svg viewBox="0 0 200 200" className={styles.heroIcon}>
            <path
              d="M40,60 Q60,30 80,60 T120,60"
              stroke="currentColor"
              strokeWidth="2"
              fill="none"
              className={styles.heroPath1}
            />
            <path
              d="M60,100 Q80,70 100,100 T140,100"
              stroke="currentColor"
              strokeWidth="2"
              fill="none"
              className={styles.heroPath2}
            />
            <circle
              cx="100"
              cy="80"
              r="8"
              stroke="currentColor"
              strokeWidth="2"
              fill="none"
              className={styles.heroCircle}
            />
            <rect
              x="90"
              y="90"
              width="20"
              height="30"
              rx="3"
              stroke="currentColor"
              strokeWidth="2"
              fill="none"
              className={styles.heroRect}
            />
            <path
              d="M85,120 L115,120"
              stroke="currentColor"
              strokeWidth="2"
              className={styles.heroPath3}
            />
          </svg>
        </div>
      </div>
    </section>
  );
}