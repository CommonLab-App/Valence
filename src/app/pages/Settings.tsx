import { useId } from 'react'
import { SELECT_CLASS, Settings as ShellSettings } from '@commonlab/shell'
import { useAppState } from '@/app/AppState'
import { VALENCE_LEVELS, type Prefs } from '@/app/preferences'
import { storage } from '@/app/progress/storage'

/** The shared shell's settings page, with ValenceLab's display level under dark mode and reduced motion. */
export function Settings() {
  const state = useAppState()
  const { prefs, updatePrefs } = state
  const levelId = useId()

  return (
    <ShellSettings
      state={state}
      storage={storage}
      extraDisplay={
        <div className="flex items-center justify-between gap-4">
          <label htmlFor={levelId}>Valence display level</label>
          <select
            id={levelId}
            className={SELECT_CLASS}
            value={prefs.valenceLevel}
            onChange={(e) => updatePrefs({ valenceLevel: Number(e.target.value) as Prefs['valenceLevel'] })}
          >
            {VALENCE_LEVELS.map(({ value, label }) => (
              <option key={value} value={value}>
                {label}
              </option>
            ))}
          </select>
        </div>
      }
    />
  )
}
