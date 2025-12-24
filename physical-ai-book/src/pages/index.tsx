import type {ReactNode} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import ModuleGrid from '@site/src/components/ModuleGrid/ModuleGrid';
import HeroSection from '@site/src/components/HeroSection';

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="Connecting AI Agents with Humanoid Robotics - A comprehensive curriculum for advanced robotics and AI integration">
      <main>
        <HeroSection
          tagline="ADVANCED ROBOTICS & AI"
          title={siteConfig.title}
          subtitle={siteConfig.tagline}
          ctaText="Start Learning"
          ctaLink="/docs/modules/module-01-ros2/intro"
          secondaryCtaText="View Curriculum"
          secondaryCtaLink="/docs/intro"
        />
        <ModuleGrid />
      </main>
    </Layout>
  );
}
