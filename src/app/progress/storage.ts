// ValenceLab's saved data, made by the shared shell (@commonlab/shell) under the `valence:` prefix. What is stored,
// and how, is the shell's; the entries ValenceLab saves are listed here.
import { createStorage, PREFS_ENTRY } from '@commonlab/shell/core'

export { createMemoryStore, readEntry, sessionStore, type ActivityStatus, type KeyValueStore, type SessionStore } from '@commonlab/shell/core'

export const ENTRY = {
  prefs: PREFS_ENTRY,
  titration: 'lab:titration',
  aqueous: 'lab:aqueous',
  flame: 'lab:flame',
  calorimetry: 'lab:calorimetry',
  cations: 'lab:cations',
  lechatelier: 'lab:le-chatelier',
  clock: 'lab:clock-reaction',
  acetone: 'lab:iodination-of-acetone',
  cabbage: 'lab:red-cabbage-ph',
  density: 'lab:measurement-and-density',
  freezing: 'lab:freezing-point-depression',
  reactions: 'lab:types-of-reactions',
  mixing: 'lab:polarity-and-mixing',
  hotcold: 'lab:endothermic-and-exothermic',
  mechanism: 'mechanism:hcl-nahco3',
} as const

// "Valence" is the short name, as body text says it (NAMING.md); the tab title says ValenceLab (AppState.tsx).
export const storage = createStorage({ prefix: 'valence:', name: 'Valence' })

export const { storageKey, browserStore, saveEntry, loadEntry, peekStatus, wasSetAside, exportAll, clearAll, NOT_SAVING_TEXT } = storage
