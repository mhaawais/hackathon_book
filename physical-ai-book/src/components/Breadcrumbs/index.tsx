import React from 'react';
import Link from '@docusaurus/Link';
import { useLocation } from '@docusaurus/router';
import styles from './styles.module.css';

interface Breadcrumb {
  label: string;
  href?: string;
}

interface BreadcrumbsProps {
  className?: string;
}

export default function Breadcrumbs({ className }: BreadcrumbsProps): JSX.Element | null {
  const location = useLocation();

  // Skip breadcrumbs on homepage and certain pages
  if (location.pathname === '/' || location.pathname === '/docs') {
    return null;
  }

  // Generate breadcrumbs based on the URL path
  const pathSegments = location.pathname
    .split('/')
    .filter(segment => segment !== '')
    .map(segment => ({
      segment,
      label: segment
        .replace(/-/g, ' ')
        .replace(/\b\w/g, l => l.toUpperCase()),
    }));

  // Add special handling for docs pages
  if (location.pathname.startsWith('/docs/')) {
    const docsPath = location.pathname.replace('/docs/', '');
    const segments = docsPath.split('/').filter(s => s);

    if (segments.length > 0) {
      // Create a more meaningful breadcrumb trail for docs
      const breadcrumbs: Breadcrumb[] = [
        { label: 'Modules', href: '/docs' }
      ];

      // Add intermediate segments
      let currentPath = '/docs';
      segments.forEach((segment, index) => {
        currentPath += `/${segment}`;

        // Try to get a better label from frontmatter or metadata if available
        let label = segment
          .replace(/-/g, ' ')
          .replace(/\b\w/g, l => l.toUpperCase());

        // If this is the last segment, use a special approach to get the title
        // In a real implementation, we'd need to get the title from the page metadata
        breadcrumbs.push({ label, href: currentPath });
      });

      return (
        <nav className={`${styles.breadcrumbs} ${className || ''}`} aria-label="breadcrumbs">
          <ol className={styles.breadcrumbList}>
            <li className={styles.breadcrumbItem}>
              <Link to="/" className={styles.breadcrumbLink}>
                Home
              </Link>
            </li>
            {breadcrumbs.map((crumb, index) => (
              <li key={index} className={styles.breadcrumbItem}>
                <span className={styles.breadcrumbSeparator}>/</span>
                {crumb.href && index < breadcrumbs.length - 1 ? (
                  <Link to={crumb.href} className={styles.breadcrumbLink}>
                    {crumb.label}
                  </Link>
                ) : (
                  <span className={styles.breadcrumbCurrent}>{crumb.label}</span>
                )}
              </li>
            ))}
          </ol>
        </nav>
      );
    }
  }

  // Fallback for other pages
  const breadcrumbs: Breadcrumb[] = [
    { label: 'Home', href: '/' }
  ];

  let currentPath = '';
  pathSegments.forEach((segment, index) => {
    currentPath += `/${segment.segment}`;
    breadcrumbs.push({
      label: segment.label,
      href: currentPath
    });
  });

  return (
    <nav className={`${styles.breadcrumbs} ${className || ''}`} aria-label="breadcrumbs">
      <ol className={styles.breadcrumbList}>
        {breadcrumbs.map((crumb, index) => (
          <li key={index} className={styles.breadcrumbItem}>
            {index > 0 && <span className={styles.breadcrumbSeparator}>/</span>}
            {crumb.href && index < breadcrumbs.length - 1 ? (
              <Link to={crumb.href} className={styles.breadcrumbLink}>
                {crumb.label}
              </Link>
            ) : (
              <span className={styles.breadcrumbCurrent}>{crumb.label}</span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}