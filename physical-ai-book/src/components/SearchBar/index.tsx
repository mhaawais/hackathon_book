import React, { useState, useEffect, useRef } from 'react';
import Link from '@docusaurus/Link';
import { useLocation } from '@docusaurus/router';
import { DocSearchButton, useDocSearchKeyboardEvents } from '@docusaurus/theme-common';
import styles from './styles.module.css';

interface SearchBarProps {
  show: boolean;
  onClose: () => void;
}

export default function SearchBar({ show, onClose }: SearchBarProps) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<any[]>([]);
  const [activeIndex, setActiveIndex] = useState(-1);
  const inputRef = useRef<HTMLInputElement>(null);
  const location = useLocation();

  // Focus input when search bar is shown
  useEffect(() => {
    if (show && inputRef.current) {
      inputRef.current.focus();
    }
  }, [show]);

  // Close search when route changes
  useEffect(() => {
    onClose();
  }, [location.pathname, onClose]);

  // Keyboard navigation for results
  useEffect(() => {
    if (!show) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        setActiveIndex(prev => Math.min(prev + 1, results.length - 1));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setActiveIndex(prev => Math.max(prev - 1, 0));
      } else if (e.key === 'Enter' && activeIndex >= 0) {
        e.preventDefault();
        // Simulate click on active result
        const result = results[activeIndex];
        if (result) {
          window.location.href = result.url;
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [show, results, activeIndex]);

  // Mock search function - in a real implementation, this would call an API
  const performSearch = (searchQuery: string) => {
    if (searchQuery.trim() === '') {
      setResults([]);
      return;
    }

    // This is a placeholder - in a real implementation, you would connect to Algolia or another search provider
    const mockResults = [
      {
        title: 'Getting Started with ROS 2',
        url: '/docs/modules/module-01-ros2/intro',
        summary: 'Introduction to ROS 2 as the communication backbone for humanoid robotics'
      },
      {
        title: 'ROS 2 Fundamentals',
        url: '/docs/modules/module-01-ros2/chapter-01-ros2-fundamentals',
        summary: 'Core concepts of ROS 2 including nodes, topics, and services'
      },
      {
        title: 'Digital Twin Simulation',
        url: '/docs/modules/module-02-digital-twin/intro',
        summary: 'Physics-based simulation using Gazebo and Unity for humanoid robots'
      },
      {
        title: 'AI Robot Brain with Isaac',
        url: '/docs/modules/module-03-isaac/intro',
        summary: 'Perception, navigation, and training using NVIDIA Isaac'
      },
      {
        title: 'Vision-Language-Action Systems',
        url: '/docs/modules/module-04-vla/intro',
        summary: 'Integration of speech, vision, and planning for autonomous robots'
      }
    ];

    const filteredResults = mockResults.filter(item =>
      item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.summary.toLowerCase().includes(searchQuery.toLowerCase())
    );

    setResults(filteredResults);
    setActiveIndex(-1);
  };

  useEffect(() => {
    performSearch(query);
  }, [query]);

  if (!show) return null;

  return (
    <div className={styles.searchOverlay} onClick={onClose}>
      <div className={styles.searchContainer} onClick={(e) => e.stopPropagation()}>
        <div className={styles.searchHeader}>
          <input
            ref={inputRef}
            type="text"
            className={styles.searchInput}
            placeholder="Search documentation..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Escape') {
                onClose();
              }
            }}
          />
          <button className={styles.closeButton} onClick={onClose}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 18L18 6M6 6L18 18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
        </div>
        <div className={styles.searchHint}>
          <span>ESC to close</span>
          <span>↑↓ to navigate</span>
          <span>⏎ to select</span>
        </div>
        <div className={styles.searchResults}>
          {results.length > 0 ? (
            results.map((result, index) => (
              <Link
                key={result.url}
                to={result.url}
                className={`${styles.searchResult} ${index === activeIndex ? styles.activeResult : ''}`}
                onClick={onClose}
              >
                <h3 className={styles.resultTitle}>{result.title}</h3>
                <p className={styles.resultSummary}>{result.summary}</p>
              </Link>
            ))
          ) : query.trim() === '' ? (
            <div className={styles.emptyState}>
              <p>Search across the Physical AI curriculum</p>
            </div>
          ) : (
            <div className={styles.emptyState}>
              <p>No results found for "{query}"</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}