import NamedBo from "./NamedBo";

export default class Examtypebo extends NamedBo{

	constructor() {
		super();

	  }
	
	  
	  static fromJSON(examtype) {
		let result = [];
	
		if (Array.isArray(examtype)) {
			examtype.forEach((a) => {
			Object.setPrototypeOf(a, Examtypebo.prototype);
			result.push(a);
		  })
		} else {
		  // Es handelt sich offenbar um ein singuläres Objekt
		  let a = examtype;
		  Object.setPrototypeOf(a, Examtypebo.prototype);
		  result.push(a);
		}
	
		return result;
	  }
	}