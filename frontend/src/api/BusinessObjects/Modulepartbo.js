import SpoElementbo from "./SpoElementbo";

export default class Modulepartbo extends SpoElementbo {
  /**
   * Constructs a new Modulepartbo object with a given owner.
   */
  constructor() {
    super();
    this.sws = null;
    this.language = null;
    this.description = null;
    this.connection = null;
    this.literature = null;
    this.sources = null;
    this.semester = null;
    this.professor = null;
  }

  /**
   * Sets the owner of this Modulepartbo.
   *
   * @param {*} aSws - the new owner of this Modulepartbo.
   */
  setSws(aSws) {
    this.sws = aSws;
  }

  /**
   * Gets the owner of this Modulepartbo.
   */
  getSws() {
    return this.sws;
  }

  /**
   * Sets the owner of this Modulepartbo.
   *
   * @param {*} aLanguage - the new owner of this Modulepartbo.
   */
  setLanguage(aLanguage) {
    this.language = aLanguage;
  }

  /**
   * Gets the owner of this Modulepartbo.
   */
  getLanguage() {
    return this.language;
  }

  /**
   * Sets the owner of this Modulepartbo.
   *
   * @param {*} aDescription - the new owner of this Modulepartbo.
   */
  setDescription(aDescription) {
    this.description = aDescription;
  }

  /**
   * Gets the owner of this Modulepartbo.
   */
  getDescription() {
    return this.description;
  }

  /**
   * Sets the owner of this Modulepartbo.
   *
   * @param {*} aConnection - the new owner of this Modulepartbo.
   */
  setConnection(aConnection) {
    this.connection = aConnection;
  }

  /**
   * Gets the owner of this Modulepartbo.
   */
  getConnection() {
    return this.connection;
  }

  /**
   * Sets the owner of this Modulepartbo.
   *
   * @param {*} aLiterature - the new owner of this Modulepartbo.
   */
  setLiterature(aLiterature) {
    this.literature = aLiterature;
  }

  /**
   * Gets the owner of this Modulepartbo.
   */
  getLiterature() {
    return this.literature;
  }

  /**
   * Sets the owner of this Modulepartbo.
   *
   * @param {*} aSources - the new owner of this Modulepartbo.
   */
  setSources(aSources) {
    this.sources = aSources;
  }

  /**
   * Gets the owner of this Modulepartbo.
   */
  getSources() {
    return this.sources;
  }

  /**
   * Sets the owner of this Modulepartbo.
   *
   * @param {*} aSemester - the new owner of this Modulepartbo.
   */
  setSemester(aSemester) {
    this.semester = aSemester;
  }

  /**
   * Gets the owner of this Modulepartbo.
   */
  getSemester() {
    return this.semester;
  }

  /**
   * Sets the owner of this Modulepartbo.
   *
   * @param {*} aProfessor - the new owner of this Modulepartbo.
   */
  setProfessor(aProfessor) {
    this.professor = aProfessor;
  }

  /**
   * Gets the owner of this Modulepartbo.
   */
  getProfessor() {
    return this.professor;
  }

  /**
   * Returns an Array of Modulepartbo from a given JSON structure
   */
  static fromJSON(modulepart) {
    let result = [];

    if (Array.isArray(modulepart)) {
      modulepart.forEach((a) => {
        Object.setPrototypeOf(a, Modulepartbo.prototype);
        result.push(a);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = modulepart;
      Object.setPrototypeOf(a, Modulepartbo.prototype);
      result.push(a);
    }

    return result;
  }
}
