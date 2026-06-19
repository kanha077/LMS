# Sahayta — Stitch Design Prompt

---

## 🎯 Product Context

**Product name:** Sahayta (Sanskrit for "Help / Support")
**Product type:** Learning Management System (LMS)
**Tagline:** *Limitless education, effortless management.*
**Audience:** Educators, institutions, corporate trainers, independent course creators
**Tone:** Trustworthy, modern, empowering — not corporate, not playful. Confident and calm.

---

## 🎨 Visual Identity

### Color Palette

| Role | Color | Hex |
|---|---|---|
| Primary Brand | Deep Indigo | `#1E1B4B` |
| Accent / CTA | Saffron Gold | `#F59E0B` |
| Accent Hover | Amber | `#D97706` |
| Surface Light | Pure White | `#FFFFFF` |
| Surface Muted | Warm Gray | `#F8F7FF` |
| Text Primary | Near Black | `#0F0E1A` |
| Text Secondary | Cool Gray | `#6B7280` |
| Border | Soft Indigo Tint | `#E8E7F5` |
| Success | Teal Green | `#059669` |
| Danger | Coral Red | `#DC2626` |

> **Rule:** Indigo is structural (navbars, sidebars, headers). Saffron is always intentional — used only for primary CTAs, active states, and key highlights. Never use both on the same element.

---

### Typography

| Role | Font | Weight | Size |
|---|---|---|---|
| Display / Hero | Playfair Display | 700 Bold | 48–64px |
| Section Headings | Inter | 600 SemiBold | 28–36px |
| Card Titles | Inter | 500 Medium | 18–20px |
| Body / Paragraphs | Inter | 400 Regular | 15–16px |
| Labels / Captions | Inter | 400 Regular | 12–13px |
| Navigation | Inter | 500 Medium | 14px |
| Buttons | Inter | 600 SemiBold | 14–15px |

---

### Shape & Spacing

- **Border radius:** 12px for cards, 8px for inputs and badges, 50px for pill buttons
- **Shadows:** Subtle only — `0 1px 4px rgba(30,27,75,0.08)` for cards. No heavy drop shadows.
- **Spacing system:** 4px base unit — use multiples of 4 (8, 12, 16, 24, 32, 48, 64px)
- **No glassmorphism** on core UI elements — reserve frosted glass only for modal overlays if needed

---

## 🖥️ Pages to Design

---

### 1. Landing Page (Marketing / Public)

**Layout:** Full-width, single scroll

**Navbar:**
- Left: Sahayta wordmark in Playfair Display, Deep Indigo
- Right: Navigation links (Features, Pricing, About) in Inter 14px + "Get Started" pill button in Saffron Gold with white text

**Hero Section:**
- Background: Deep Indigo `#1E1B4B`
- Headline (Playfair Display, 60px, white): *"The Modern Operating System for Education"*
- Subheadline (Inter, 18px, `#C4C2E8`): *"Build courses, engage learners, and scale your impact — all from one beautifully simple platform."*
- Two CTA buttons: "Start for Free" (Saffron filled, pill) + "See a Demo" (white outline, pill)
- Hero visual (right side): Dashboard screenshot or abstract 3D UI mockup with indigo-to-saffron gradient glow

**Stats Bar:**
- White background strip with 3 metrics in Inter: `50,000+ Learners` | `2,000+ Courses` | `98% Satisfaction`
- Numbers in Playfair Display, Deep Indigo. Labels in Cool Gray.

**Features Section (3-column card grid):**
- White background
- Section label (small caps, Saffron): WHAT WE OFFER
- Section heading (Inter 600, 36px, Indigo): *"Everything educators need, nothing they don't"*
- 3 feature cards with icon + title + 2-line description:
  1. 🧩 *Drag-and-Drop Course Builder* — Build comprehensive curriculums in minutes
  2. 📊 *Real-Time Analytics* — Track student progress, completion rates, and grades
  3. 🏛️ *Multi-Tenant Architecture* — Manage multiple institutions from one dashboard
- Card style: White, 12px radius, 1px border `#E8E7F5`, subtle shadow, Saffron icon accent color

**Social Proof / Testimonial:**
- Light warm-gray background `#F8F7FF`
- One large quote in Playfair Display italic, Deep Indigo
- Educator name + institution in Inter, Cool Gray below

**Final CTA Section:**
- Deep Indigo background
- Headline (Playfair, white): *"Ready to transform how you teach?"*
- Single "Get Started Free" Saffron pill button, centered

**Footer:**
- Dark Indigo `#141232`
- Logo left, links center, social icons right
- All text in muted `#9896B8`

---

### 2. Dashboard (Educator Home — Post Login)

**Layout:** Left sidebar + main content area

**Sidebar (280px wide):**
- Background: Deep Indigo `#1E1B4B`
- Top: Sahayta wordmark (white) + institution name below in `#9896B8`
- Nav items with Tabler outline icons: Dashboard, My Courses, Students, Analytics, Assignments, Settings
- Active state: Saffron left border (3px) + saffron text + very subtle white-5% row background
- Inactive: White 70% opacity text, no background
- Bottom: User avatar + name + "Logout" small link

**Top Bar:**
- White background, 1px bottom border `#E8E7F5`
- Left: Page title "Good morning, Priya 👋" in Inter 600 24px, Indigo
- Right: Notification bell icon + search bar (rounded input, 40px height)

**Stats Row (4 metric cards):**
- Cards: White bg, 12px radius, subtle shadow
- Metrics: Total Students | Active Courses | Avg. Completion Rate | Pending Assignments
- Number in Playfair Display 32px Indigo, label below in Inter 13px Cool Gray
- Small trend indicator (↑ 12% this month) in Teal Green

**Recent Courses Grid (2 columns):**
- Section heading "Your Courses" in Inter 600 20px + "View All →" link in Saffron on right
- Course cards: Thumbnail image top (16:9, rounded top corners) + course title + student count + progress bar in Saffron + "Edit" button

**Student Activity Table:**
- Clean table: Student Name | Course | Last Active | Progress | Status
- Status badges: "On Track" (teal bg, teal text) | "At Risk" (amber bg, amber text) | "Completed" (light green)
- Row hover: very light indigo tint `#F4F3FF`

---

### 3. Course Builder Page

**Layout:** Full screen, no sidebar — focused editing mode

**Top Bar:**
- Left: Back arrow + course title (editable inline, Inter 500 18px)
- Right: "Preview" ghost button + "Publish Course" Saffron filled button + autosave indicator ("Saved just now" in Cool Gray)

**Left Panel (Module Tree, 260px):**
- Background `#F8F7FF`
- Section list with drag handles (⠿ icon)
- Active section: Saffron left accent, Indigo text
- "+ Add Section" button at bottom, dashed border style

**Main Canvas (Center):**
- White background
- Current lesson editor: Rich text area (prose, not a toolbar-heavy editor)
- Below text: Media embed blocks — Video, Image, Quiz, File upload as horizontal pill buttons in `#E8E7F5`
- Clean, distraction-free — minimal chrome

**Right Panel (Lesson Settings, 280px):**
- Background White, left border `#E8E7F5`
- Fields: Lesson Title, Duration estimate, Prerequisites dropdown, Visibility toggle
- All inputs: 8px radius, 1px border `#E8E7F5`, focus state with Saffron outline

---

### 4. Analytics Dashboard

**Layout:** Sidebar + full content area with charts

**Header:**
- "Analytics Overview" in Inter 600 28px + date range picker (last 7d / 30d / custom)

**Top KPI Cards (4 cards):**
- Total Enrollments | Course Completion Rate | Avg. Quiz Score | New Students This Month
- Same metric card style as Dashboard

**Charts Row:**
- Left (60%): Line chart — Student activity over time, Indigo line with Saffron hover points
- Right (40%): Donut chart — Completion rate breakdown (Completed / In Progress / Not Started) in Teal, Saffron, Cool Gray

**Bottom Table:**
- "Course Performance" — sortable columns: Course Name | Enrolled | Completed | Avg. Score | Last Updated
- Clean table, no zebra striping — rely on hover states only

---

### 5. Student View (Course Player)

**Layout:** Sidebar (course outline) + main video/content area

**Left Sidebar:**
- White bg, module list with checkmarks (✓ Saffron for completed, gray circle for incomplete)
- Current lesson highlighted: Indigo background, white text

**Main Content:**
- Video player (full width of content area, dark chrome)
- Below: Lesson title in Playfair 28px + description in Inter body
- Navigation: "← Previous Lesson" | "Next Lesson →" buttons at bottom
- On final lesson: "Mark as Complete" Saffron pill button, centered

---

## ✅ Global Design Rules for All Pages

1. **Never use more than 2 accent colors per screen.** Indigo for structure, Saffron for action — that's it.
2. **All primary CTAs are Saffron pill buttons.** Secondary actions are Indigo outline or ghost.
3. **No gradients on interactive elements.** Gradients only allowed in hero backgrounds or decorative illustrations.
4. **Icons:** Tabler outline icon set throughout. Consistent 20px size in UI, 24px in empty states.
5. **Empty states:** Always include an illustration (simple, line-art style in Indigo) + a helpful action button.
6. **Loading states:** Skeleton screens (gray shimmer), not spinners.
7. **Mobile:** All pages must be responsive. Sidebar collapses to bottom tab bar on mobile. Cards go single column.
8. **Elevation:** Only 2 levels — flat (no shadow) for containers, subtle shadow for interactive cards.
9. **Form inputs:** 44px height minimum, always labeled above (never placeholder-only).
10. **Typography contrast:** Body text is always `#0F0E1A` on white. Never use Cool Gray `#6B7280` for anything longer than a caption.
