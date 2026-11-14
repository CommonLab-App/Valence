// With their extensions, here and in preferences.ts: vite.config.ts imports this file, and Vite asks that of what its config imports.
import { firstPaintScript as scriptFor } from '@commonlab/shell/core'
import { PREF_VALUES } from './preferences.ts'
import { ENTRY, storageKey } from './progress/storage.ts'

export { applyAppearance, storedAppearance } from '@commonlab/shell/core'

/** The script index.html runs before first paint, for ValenceLab's stored preferences (vite.config.ts puts it there). */
export const firstPaintScript = () => scriptFor(storageKey(ENTRY.prefs), PREF_VALUES)
