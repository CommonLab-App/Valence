import { createAppState } from '@commonlab/shell'
import { prefs } from './preferences'
import { storage } from './progress/storage'

export const { AppStateProvider, useAppState } = createAppState({ storage, prefs, title: 'ValenceLab' })
