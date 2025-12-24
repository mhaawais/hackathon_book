import React from 'react';
import clsx from 'clsx';
import ModuleCard from '../ModuleCard/ModuleCard';
import styles from './styles.module.css';

interface ModuleGridProps {
  className?: string;
}

export default function ModuleGrid({ className }: ModuleGridProps): JSX.Element {
  const modules = [
    {
      number: '1',
      title: 'The Robotic Nervous System (ROS 2)',
      description: 'Introduction to ROS 2 as the communication backbone for humanoid robotics, covering nodes, topics, services, and integration with AI agents.',
      to: '/docs/modules/module-01-ros2/intro',
    },
    {
      number: '2',
      title: 'The Digital Twin (Gazebo & Unity)',
      description: 'Physics-based simulation and environment building for humanoid robots using Gazebo for realistic dynamics and Unity for high-fidelity interaction.',
      to: '/docs/modules/module-02-digital-twin/intro',
    },
    {
      number: '3',
      title: 'The AI-Robot Brain (NVIDIA Isaac™)',
      description: 'Perception, navigation, and training systems using NVIDIA Isaac to enable humanoid autonomy with VSLAM and Nav2 path planning.',
      to: '/docs/modules/module-03-isaac/intro',
    },
    {
      number: '4',
      title: 'Vision-Language-Action (VLA)',
      description: 'Integration of speech, vision, and planning capabilities for humanoid robots to understand natural language commands and act autonomously.',
      to: '/docs/modules/module-04-vla/intro',
    },
  ];

  return (
    <section className={clsx(styles.moduleGrid, className)}>
      <div className="container">
        <div className="row">
          {modules.map((module, index) => (
            <div key={index} className={clsx('col', 'col--6', styles.moduleCol)}>
              <ModuleCard
                number={module.number}
                title={module.title}
                description={module.description}
                to={module.to}
              />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}