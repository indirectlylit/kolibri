import KButton from 'kolibri.coreVue.components.KButton';
import KCheckbox from 'kolibri.coreVue.components.KCheckbox';
import KDropdownMenu from 'kolibri.coreVue.components.KDropdownMenu';
import KGrid from 'kolibri.coreVue.components.KGrid';
import KGridItem from 'kolibri.coreVue.components.KGridItem';
import KRouterLink from 'kolibri.coreVue.components.KRouterLink';
import KSelect from 'kolibri.coreVue.components.KSelect';
import { coachStringsMixin } from './shared/commonCoachStrings';
import Answer from './shared/Answer';
import BackLink from './shared/BackLink';
import Completed from './shared/status/Completed';
import TruncatedItemList from './shared/TruncatedItemList';
import InProgress from './shared/status/InProgress';
import LessonActive from './shared/LessonActive';
import MasteryModel from './shared/MasteryModel';
import NeedHelp from './shared/status/NeedHelp';
import NotStarted from './shared/status/NotStarted';
import Recipients from './shared/Recipients';
import Score from './shared/Score';
import Started from './shared/status/Started';
import TimeDuration from './shared/TimeDuration';
import QuizActive from './shared/QuizActive';

export default {
  name: 'ReportsQuizHeader',
  components: {
    KButton,
    KCheckbox,
    KDropdownMenu,
    KGrid,
    KGridItem,
    KRouterLink,
    KSelect,
    Answer,
    BackLink,
    Completed,
    TruncatedItemList,
    InProgress,
    LessonActive,
    MasteryModel,
    NeedHelp,
    NotStarted,
    Recipients,
    Score,
    Started,
    TimeDuration,
    QuizActive,
  },
  mixins: [coachStringsMixin],
  methods: {
    newCoachRoute(page) {
      return { name: 'NEW_COACH_PAGES', params: { page } };
    },
  },
};