// ValenceLab's preferences: the shared shell's dark mode and reduced motion, and the valence display level.
// With its extensions, here and in firstPaint.ts: vite.config.ts imports this file, and Vite asks that of what its config imports.
import { createPreferences } from '@commonlab/shell/core'
import { storage } from './progress/storage.ts'

export { PREFS_VERSION, resolveTri, type Tri } from '@commonlab/shell/core'

export const prefs = createPreferences(storage, { values: { valenceLevel: [1, 2, 3] }, defaults: { valenceLevel: 2 } })

export const { PREF_VALUES, DEFAULT_PREFS, loadPrefs, savePrefs } = prefs

export type Prefs = ReturnType<typeof prefs.loadPrefs>

/** The valence display levels (spec 6.4) as the level controls list them. */
export const VALENCE_LEVELS: readonly { value: Prefs['valenceLevel']; label: string }[] = [
  { value: 1, label: '1: Bohr shells' },
  { value: 2, label: '2: Lewis dots' },
  { value: 3, label: '3: Orbitals' },
]
