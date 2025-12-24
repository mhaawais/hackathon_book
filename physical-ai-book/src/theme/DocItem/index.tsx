import React from 'react';
import DocItem from '@theme-original/DocItem';
import Breadcrumbs from '@site/src/components/Breadcrumbs';

export default function DocItemWrapper(props) {
  return (
    <>
      <Breadcrumbs />
      <div className="doc-article-container">
        <DocItem {...props} />
      </div>
    </>
  );
}