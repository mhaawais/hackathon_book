import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import {useCurrentSidebarCategory, useThemeConfig} from '@docusaurus/theme-common';
import {translate} from '@docusaurus/Translate';
import styles from './styles.module.css';

function DocSidebarItemCategory({item, onItemClick, active, level, index, ...props}) {
  const {items, label, collapsible, className} = item;
  const [collapsed, setCollapsed] = React.useState(item.collapsed);
  const [isControlled, setIsControlled] = React.useState(false);
  const toggleCollapsed = React.useCallback(() => {
    if (!isControlled) {
      setIsControlled(true);
    }
    setCollapsed((state) => !state);
  }, [isControlled]);
  React.useEffect(() => {
    if (isControlled) {
      return;
    }
    setCollapsed(item.collapsed);
  }, [isControlled, item.collapsed]);
  const {
    docs: {sidebar: sidebarPreference},
  } = useThemeConfig();
  const sidebarCollapsed =
    collapsible && sidebarPreference !== 'promoteSidebar' && collapsed;
  const baseClassName = 'menu__list-item';
  const categoryClassName = clsx(baseClassName, {
    'menu__list-item--collapsed': sidebarCollapsed,
  });
  const menuListClassName = 'menu__list';
  const content = (
    <>
      <div
        className={clsx('menu__list-item-collapsible', {
          'menu__list-item-collapsible--active': active,
        })}>
        <Link
          className={clsx('menu__link', {
            'menu__link--sublist': true,
            'menu__link--sublist-caret': collapsible,
            'menu__link--active': active,
          })}
          onClick={
            collapsible
              ? (e) => {
                  e.preventDefault();
                  toggleCollapsed();
                }
              : undefined
          }
          href={collapsible ? '#' : undefined}
          aria-label={
            collapsible
              ? translate(
                  {
                    id: 'theme.docs.sidebar.collapseCategoryAriaLabel',
                    message: 'Collapse sidebar category \'{label}\'',
                    values: {label},
                  },
                  {label},
                )
              : undefined
          }>
          <div className={styles.sidebarCategoryHeader}>
            <div className={styles.sidebarCategoryIcon}>
              {level === 0 && (
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M2 17L12 22L22 17" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M2 12L12 17L22 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              )}
              {level === 1 && (
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 7L10 2L16 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <rect x="4" y="7" width="16" height="14" rx="2" stroke="currentColor" strokeWidth="2"/>
                  <path d="M9 12H15" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
                  <path d="M9 16H15" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
                </svg>
              )}
            </div>
            <span className={styles.sidebarCategoryLabel}>{label}</span>
          </div>
        </Link>
        {collapsible && (
          <div
            className={clsx('menu__caret', {
              'menu__caret--collapsed': sidebarCollapsed,
            })}
            onClick={(e) => {
              e.preventDefault();
              toggleCollapsed();
            }}
          />
        )}
      </div>
      <ul className={menuListClassName}>
        {items.map((childItem, childIndex) => (
          <DocSidebarItem
            key={childIndex}
            active={childItem.active}
            index={childIndex}
            onItemClick={onItemClick}
            level={level + 1}
            item={childItem}
            {...props}
          />
        ))}
      </ul>
    </>
  );
  return <li className={categoryClassName}>{content}</li>;
}

function DocSidebarItemLink({item, onItemClick, active, level}) {
  const {href, label, className} = item;
  return (
    <li className="menu__list-item">
      <Link
        className={clsx('menu__link', {
          'menu__link--active': active,
        })}
        to={href}
        {...(active && {ariaCurrent: 'page'})}
        onClick={onItemClick}>
        <div className={styles.sidebarItemLink}>
          {level > 0 && (
            <span className={styles.sidebarItemBullet}>•</span>
          )}
          <span className={styles.sidebarItemText}>{label}</span>
        </div>
      </Link>
    </li>
  );
}

export default function DocSidebarItem(props) {
  const {item} = props;
  switch (item.type) {
    case 'category':
      return <DocSidebarItemCategory {...props} />;
    case 'link':
    default:
      return <DocSidebarItemLink {...props} />;
  }
}