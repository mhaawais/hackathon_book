import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './404.module.css';

export default function NotFound(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout title={`Page Not Found | ${siteConfig.title}`} description="The requested page could not be found">
      <main className={styles.notFoundPage}>
        <div className={styles.notFoundContainer}>
          <div className={styles.heroGraphic}>
            <svg viewBox="0 0 200 200" className={styles.errorIcon}>
              <path
                d="M40,60 Q60,30 80,60 T120,60"
                stroke="currentColor"
                strokeWidth="2"
                fill="none"
              />
              <path
                d="M60,100 Q80,70 100,100 T140,100"
                stroke="currentColor"
                strokeWidth="2"
                fill="none"
              />
              <circle
                cx="100"
                cy="80"
                r="8"
                stroke="currentColor"
                strokeWidth="2"
                fill="none"
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
              />
              <path
                d="M85,120 L115,120"
                stroke="currentColor"
                strokeWidth="2"
              />
            </svg>
          </div>
          <h1 className={styles.notFoundTitle}>
            <span className={styles.errorCode}>404</span>
            <span className={styles.errorText}>Page Not Found</span>
          </h1>
          <p className={styles.notFoundMessage}>
            Oops! The page you're looking for doesn't exist or has been moved.
          </p>
          <div className={styles.notFoundActions}>
            <Link className="button button--primary button--lg" to="/">
              Go to Homepage
            </Link>
            <Link className="button button--secondary button--lg" to="/docs/intro">
              Browse Documentation
            </Link>
          </div>
        </div>
      </main>
    </Layout>
  );
}