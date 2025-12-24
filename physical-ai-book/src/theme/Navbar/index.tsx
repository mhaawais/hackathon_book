import React, { useState, useEffect } from 'react';
import Navbar from '@theme-original/Navbar';
import SearchBar from '@site/src/components/SearchBar';

// Add mobile navigation enhancements and search functionality
export default function NavbarWrapper(props) {
  const [showSearch, setShowSearch] = useState(false);

  // Add keyboard shortcut for search (Cmd/Ctrl + K)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        setShowSearch(true);
      }
      if (e.key === 'Escape') {
        setShowSearch(false);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <>
      <Navbar {...props} />
      <SearchBar show={showSearch} onClose={() => setShowSearch(false)} />
    </>
  );
}