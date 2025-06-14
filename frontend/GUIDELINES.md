# Frontend Guidelines

## Design Principles
- Minimalism: Use as few UI elements as possible. Prioritize whitespace and clarity.
- Inspiration: Yeezy.com — bold, clean, and modern.
- Liquid Glass Button: Use the provided component from `/src` and ensure it is the primary interactive element.
- Responsive: Must look good on desktop and mobile.

## Code Standards
- Use React functional components and hooks.
- Use CSS modules or styled-components for styling.
- Keep components small and focused.
- Use clear, descriptive names for components and props.
- Document all components with JSDoc comments.
- Prefer composition over inheritance.

## File Organization
- Place reusable components in `frontend/src/components/`.
- Keep styles close to components.
- Use `index.js` for exports in component folders.

## Accessibility
- All interactive elements must be keyboard accessible.
- Use semantic HTML wherever possible. 