<template>
  <v-app>
    <div id="background">
      <div style="padding: 50px 0px; background: #f0f0f0;"></div>
      <!-- <Steps :Steps="Steps"></Steps> -->

      <transition-group mode="out-in">
        <AfterGoal
          key="3"
          @startGoalEdit="startGoalEdit"
          v-show="isGoalRegistered && !isGoalEditMode"
          :Goal="Goal"
        ></AfterGoal>
        <BeforeGoal
          key="1"
          @close="endGoalEdit"
          v-show="!isGoalRegistered || isGoalEditMode"
          :Goal="Goal"
          :OriginalGoal="OriginalGoal"
        ></BeforeGoal>
      </transition-group>

      <transition>
        <Kanban :Boards="Boards"></Kanban>
      </transition>

      <Note :Notes="Notes"></Note>

      <transition-group mode="out-in">
        <AfterGIveUp
          key="3"
          :Worries="Worries"
          @startGiveUpEdit="startGiveUpEdit"
          v-show="isGiveUpRegisterd && !isGiveUpEditMode"
        ></AfterGIveUp>
        <BeforeGiveUp
          :Worries="Worries"
          :OriginalWorries="OriginalWorries"
          key="1"
          @close="endGiveUpEdit"
          v-show="!isGiveUpRegisterd || isGiveUpEditMode"
        ></BeforeGiveUp>
      </transition-group>
      <!-- <div style="padding: 50px 0px; background: #f0f0f0;"></div> -->

      <transition-group mode="out-in">
        <AfterMotive
          key="3"
          @startMotiveEdit="startMotiveEdit"
          v-show="isMotiveRegisterd && !isMotiveEditMode"
          :Motives="Motives"
          :SelfTranscendence="SelfTranscendence"
          :FutureSelves="FutureSelves"
        ></AfterMotive>
        <BeforeMotive
          key="1"
          @close="endMotiveEdit"
          v-show="!isMotiveRegisterd || isMotiveEditMode"
          :Motives="Motives"
          :OriginalMotives="OriginalMotives"
          :SelfTranscendence="SelfTranscendence"
          :OriginalSelf="OriginalSelf"
          :FutureSelves="FutureSelves"
          :OriginalFuture="OriginalFuture"
        ></BeforeMotive>
      </transition-group>
    </div>
  </v-app>
</template>

<script>
import Steps from "./goal_info/Step";

// Goal
import BeforeGoal from "./goal_info/BeforeGoal";
import AfterGoal from "./goal_info/AfterGoal";

// Motive
import BeforeMotive from "./motive/BeforeMotive";
import AfterMotive from "./motive/AfterMotive";

// GiveUp
import BeforeGiveUp from "./giveup/BeforeGiveUp";
import AfterGIveUp from "./giveup/AfterGiveUp";

// Note
import Note from "./note/Note.vue";
import Kanban from "./task/Kanban.vue";

import api from "@/services/api";

export default {
  components: {
    BeforeGoal,
    AfterGoal,
    BeforeMotive,
    AfterMotive,
    BeforeGiveUp,
    AfterGIveUp,
    Note,
    Kanban,
    Steps
  },
  data: function () {
    return {
      All: {}, // For Debug
      Goal: {},
      OriginalGoal: {},

      Motives: {},
      OriginalMotives: {},

      SelfTranscendence: {},
      OriginalSelf: {},

      FutureSelves: {},
      OriginalFuture: {},

      Worries: {},
      OriginalWorries: {},

      Notes: {},
      Boards: {},
      Steps: {},

      // Componetns switch.
      isGoalRegistered: true,
      isGoalEditMode: false,

      isMotiveRegisterd: true,
      isMotiveEditMode: false,

      isGiveUpRegisterd: true,
      isGiveUpEditMode: false
    };
  },
  mounted: function () {
    let vm = this;
    // 動的に生成されたURLの"id"を取得して、そのidを元にapiでgetを投げる
    let goalId = vm.$route.params.id;
    api.get(`goals/${goalId}/`).then(function (response) {
      vm.All = response;
      // Goal_Info
      vm.$set(vm.Goal, "goal_title", response.data.goal_title);
      vm.$set(vm.Goal, "goal_description", response.data.goal_description);
      vm.$set(vm.Goal, "criteria", response.data.criteria);
      vm.$set(vm.Goal, "created_at", response.data.created_at);

      vm.$set(vm.OriginalGoal, "goal_title", response.data.goal_title);
      vm.$set(
        vm.OriginalGoal,
        "goal_description",
        response.data.goal_description
      );
      vm.$set(vm.OriginalGoal, "criteria", response.data.criteria);
      vm.$set(vm.OriginalGoal, "created_at", response.data.created_at);

      // Motive
      vm.$set(vm.Motives, "motives", response.data.motives);
      vm.$set(
        vm.OriginalMotives,
        "motives",
        // Deep Copy
        JSON.parse(JSON.stringify(vm.Motives))
      );

      // Self Transcendence Goal
      vm.$set(
        vm.SelfTranscendence,
        "self_transcendence_goals",
        response.data.self_transcendence_goals
      );
      vm.$set(
        vm.OriginalSelf,
        "self_transcendence_goals",
        // deep copy
        JSON.parse(JSON.stringify(vm.SelfTranscendence))
      );

      //  Future Selves
      vm.$set(vm.FutureSelves, "future_selves", response.data.future_selves);
      vm.$set(
        vm.OriginalFuture,
        "future_selves",
        JSON.parse(JSON.stringify(vm.FutureSelves))
      );

      //  Worry, Idea
      vm.$set(vm.Worries, "worries", response.data.worries);
      vm.$set(
        vm.OriginalWorries,
        "worries",
        JSON.parse(JSON.stringify(vm.Worries))
      );

      //  Notes
      vm.$set(vm.Notes, "notes", response.data.notes);

      // Kanban
      vm.$set(vm.Boards, "boards", response.data.boards);

      // Step
      vm.$set(vm.Steps, "steps", response.data.steps);
    });
  },
  methods: {
    startGoalEdit: function () {
      this.isGoalEditMode = true;
    },
    endGoalEdit: function () {
      this.isGoalEditMode = false;
    },

    startMotiveEdit: function () {
      this.isMotiveEditMode = true;
    },
    endMotiveEdit: function () {
      this.isMotiveEditMode = false;
    },
    startGiveUpEdit: function () {
      this.isGiveUpEditMode = true;
    },
    endGiveUpEdit: function () {
      this.isGiveUpEditMode = false;
    }
  }
};
</script>

<style lang="sass">
@import '../../assets/sass/main.scss'
</style>

<style scoped>
body {
  background: #f0f0f0;
}

#background {
  background: #f0f0f0;
}

.v-enter {
  transform: translate(-100px, 0);
  opacity: 0;
}
.v-enter-to {
  opacity: 1;
}
.v-enter-active {
  transition: all 1s 0s ease;
}
.v-leave {
  transform: translate(0, 0);
  opacity: 1;
  position: absolute;
}
.v-leave-to {
  transform: translate(-100px, 0);
  opacity: 0;
  position: absolute;
}
.v-leave-active {
  transition: all 0.5s 0s ease;
  position: absolute;
}
</style>
