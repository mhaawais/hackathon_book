import React, { useState, useEffect } from 'react';
import Link from '@docusaurus/Link';
import { useLocation } from '@docusaurus/router';
import { ThemeClassNames } from '@docusaurus/theme-common';
import styles from './styles.module.css';

interface MobileNavbarProps {
  title: string;
  logo?: {
    src: string;
    alt: string;
  };
  items: Array<{
    type: string;
    label: string;
    to?: string;
    href?: string;
    position: string;
  }>;
}

export default function MobileNavbar({ title, logo, items }: MobileNavbarProps): JSX.Element {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  // Close menu when route changes
  useEffect(() => {
    setIsOpen(false);
  }, [location.pathname]);

  // Prevent body scroll when menu is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }

    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const leftItems = items.filter(item => item.position === 'left');
  const rightItems = items.filter(item => item.position === 'right');

  return (
    <nav className={styles.mobileNavbar} role="navigation" aria-label="Main navigation">
      <div className={styles.navbarRow}>
        <div className={styles.navbarLeft}>
          <button
            className={styles.menuButton}
            onClick={toggleMenu}
            aria-label={isOpen ? "Close menu" : "Open menu"}
            aria-expanded={isOpen}
          >
            <svg
              className={styles.menuIcon}
              viewBox="0 0 24 24"
              width="24"
              height="24"
              aria-hidden="true"
            >
              {isOpen ? (
                <path
                  d="M18 6L6 18M6 6L18 18"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              ) : (
                <path
                  d="M4 6H20M4 12H20M4 18H20"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              )}
            </svg>
          </button>
          <Link to="/" className={styles.navbarLogo}>
            {logo && (
              <img src={logo.src} alt={logo.alt} className={styles.logo} />
            )}
            <span className={styles.title}>{title}</span>
          </Link>
        </div>
        <div className={styles.navbarRight}>
          {rightItems.map((item, index) => (
            <Link
              key={index}
              to={item.to || '#'}
              href={item.href}
              className={styles.navbarItem}
            >
              {item.label}
            </Link>
          ))}
        </div>
      </div>

      {/* Mobile menu overlay */}
      {isOpen && (
        <div className={styles.overlay} onClick={toggleMenu}>
          <div className={styles.menu} onClick={(e) => e.stopPropagation()}>
            <div className={styles.menuHeader}>
              <div className={styles.menuLogo}>
                {logo && (
                  <img src={logo.src} alt={logo.alt} className={styles.menuLogoImg} />
                )}
                <span className={styles.menuTitle}>{title}</span>
              </div>
              <button
                className={styles.closeButton}
                onClick={toggleMenu}
                aria-label="Close menu"
              >
                <svg
                  className={styles.closeIcon}
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  aria-hidden="true"
                >
                  <path
                    d="M18 6L6 18M6 6L18 18"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
              </button>
            </div>
            <ul className={styles.menuList}>
              {leftItems.map((item, index) => (
                <li key={index} className={styles.menuItem}>
                  <Link
                    to={item.to || '#'}
                    href={item.href}
                    className={styles.menuLink}
                    onClick={() => setIsOpen(false)}
                  >
                    {item.label}
                  </Link>
                </li>
              ))}
              {rightItems.map((item, index) => (
                <li key={`right-${index}`} className={styles.menuItem}>
                  <Link
                    to={item.to || '#'}
                    href={item.href}
                    className={styles.menuLink}
                    onClick={() => setIsOpen(false)}
                  >
                    {item.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </nav>
  );
}