import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Modules',
      collapsible: true,
      collapsed: false,
      items: [
        {
          type: 'category',
          label: 'Module 1: The Robotic Nervous System (ROS 2)',
          collapsible: true,
          collapsed: false,
          items: [
            'modules/module-01-ros2/intro',
            'modules/module-01-ros2/chapter-01-ros2-fundamentals',
            'modules/module-01-ros2/chapter-02-rclpy-ai-bridge',
            'modules/module-01-ros2/chapter-03-urdf-humanoids'
          ],
        },
        {
          type: 'category',
          label: 'Module 2: The Digital Twin',
          collapsible: true,
          collapsed: false,
          items: [
            'modules/module-02-digital-twin/intro',
            'modules/module-02-digital-twin/chapter-01-gazebo-physics',
            'modules/module-02-digital-twin/chapter-02-unity-interaction',
            'modules/module-02-digital-twin/chapter-03-sensor-simulation'
          ],
        },
        {
          type: 'category',
          label: 'Module 3: The AI-Robot Brain',
          collapsible: true,
          collapsed: false,
          items: [
            'modules/module-03-isaac/intro',
            'modules/module-03-isaac/chapter-01-isaac-sim',
            'modules/module-03-isaac/chapter-02-isaac-ros-vslam',
            'modules/module-03-isaac/chapter-03-nav2-humanoids'
          ],
        },
        {
          type: 'category',
          label: 'Module 4: Vision-Language-Action (VLA)',
          collapsible: true,
          collapsed: false,
          items: [
            'modules/module-04-vla/intro',
            'modules/module-04-vla/chapter-01-voice-to-action',
            'modules/module-04-vla/chapter-02-llm-planning',
            'modules/module-04-vla/chapter-03-capstone-autonomous-humanoid'
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'Tutorial',
      items: ['intro'],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
