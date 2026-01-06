import { render, screen } from '@testing-library/react';
import App from './App';
import { expect, test, vi } from 'vitest';

// Mock fetch
global.fetch = vi.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({}),
  })
) as any;

test('renders dashboard title', () => {
  render(<App />);
  const linkElement = screen.getByText(/Space Weather Dashboard/i);
  expect(linkElement).toBeInTheDocument();
});
